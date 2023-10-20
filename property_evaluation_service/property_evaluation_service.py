import logging
logging.basicConfig(level=logging.DEBUG)
import sys
import re
from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode, Decimal, String
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted
from data_source.data_source import DataSource
from models.property import Property, EnergyEfficiencyRating

database_path = 'db/property_database.db'

data_source = DataSource(database_path)

class PropertyEvaluationService(ServiceBase):
    @rpc(Unicode, _returns = String)
    def evaluate_property(ctx, registration_number):
        property = get_property(registration_number)
        print(property)
        compliance = get_legal_compliance_and_inspection(property)
        print(compliance)
        average_price_range = get_average_price_range(property)
        print(average_price_range)
        return str({
            'compliance': compliance,
            'average_price': list(average_price_range)
        })

# Fonction fictive pour obtenir les données du marché immobilier
def get_property(registration_number):
    property_by_registration = data_source.search_by_registration_number(registration_number)
    return property_by_registration

# Fonction fictive pour analyser les données du marché et estimer la valeur de la propriété
def get_average_price_range(property: Property):
    # Define a regular expression pattern to match the street name
    pattern = r'\d+\s+(.+)'
    # Use re.match to find the pattern in the address
    match = re.match(pattern, property.address)
    if match:
        main_street = match.group(1)
        properties = data_source.search_similar_addresses(main_street)
        if (len(properties) == 0):
            return []
        min_price = properties[0].price
        max_price = properties[0].price
        for property in properties:
            if property.price < min_price:
                min_price = property.price
            if property.price > max_price:
                max_price = property.price
        return [min_price, max_price]
    else:
        return []


# Fonction fictive pour vérifier la conformité légale et réglementaire de la propriété
def get_legal_compliance_and_inspection(property: Property):
    return {
        "dpe": property.dpe.name,
        "is_compliant": property.urbanism_compliance,
    }

application = Application([PropertyEvaluationService],
    tns='http://localhost/loan-service',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    wsgi_app = WsgiApplication(application)
    
    twisted_apps = [
        (wsgi_app, b'loan-service'),
    ]

    sys.exit(run_twisted(twisted_apps, 8080))
    