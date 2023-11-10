from flask import Flask, request, jsonify
import re
from models.property import Property, EnergyEfficiencyRating
from data_source.data_source import DataSource

database_path = 'db/property_database.db'

data_source = DataSource(database_path)

app = Flask(__name__)

# Function fictive to get property data
def get_property(registration_number):
    property_by_registration = data_source.search_by_registration_number(registration_number)
    return property_by_registration

# Function fictive to analyze market data and estimate property value
def get_average_price_range(property):
    # Define a regular expression pattern to match the street name
    pattern = r'\d+\s+(.+)'
    # Use re.match to find the pattern in the address
    match = re.match(pattern, property.address)
    if match:
        main_street = match.group(1)
        properties = data_source.search_similar_addresses(main_street)
        if not properties:
            return []
        min_price = properties[0].price
        max_price = properties[0].price
        for prop in properties:
            if prop.price < min_price:
                min_price = prop.price
            if prop.price > max_price:
                max_price = prop.price
        return [min_price, max_price]
    else:
        return []

# Function fictive to check legal compliance of the property
def get_legal_compliance_and_inspection(property):
    return {
        "dpe": property.dpe.name,
        "is_compliant": property.urbanism_compliance,
    }

@app.route('/property/evaluate/<registration_number>', methods=['GET'])
def evaluate_property(registration_number):
    property = get_property(registration_number)
    compliance = get_legal_compliance_and_inspection(property)
    average_price_range = get_average_price_range(property)

    return jsonify({
        'compliance': compliance,
        'average_price': list(average_price_range)
    })

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
