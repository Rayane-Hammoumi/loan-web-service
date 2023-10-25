import logging
logging.basicConfig(level=logging.DEBUG)
import time 
import sys
from spyne import Application, rpc, ServiceBase, Unicode, Integer, Decimal, Boolean
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted
from credit_score_service.credit_score_service import calculate_credit_score
from solvency_verification_service.solvency_verification_service import SolvencyVerificationService
from bank_db import BankDatabase

from suds.client import Client

class _loanService(ServiceBase):
    
    @rpc(Unicode, _returns=Boolean)
    def app_service(ctx, input_file):
        service_url = 'http://localhost:8080/other-service?wsdl'
        
        # Créez un client SOAP pour le service web
        client = Client(service_url)
        
        #extraire les informations du fichiers txt
        #content = _loanService().read_file_to_string(input_file)
                
        # Appelez la méthode extract_information du service TextExtractionService
        extracted_info = client.service.extract_information(input_file)  
        print(extracted_info)

        extracted_info = client.service.extract_information(input_file)  
        print(extracted_info)
        
        db = BankDatabase('client_database.db')
        client_data = db.get_client_by_id(extracted_info['Numero'])

        if client_data:
            monthly_income=client_data[2]
            monthly_expenses = client_data[3]
            unpaid_loans = client_data[4]
            current_loans = client_data[5]
            late_payments = client_data[5]
            credit_score=client.service.calculate_credit_score(unpaid_loans, current_loans, late_payments)
            is_solvent=client.service.solvency_verification_service(credit_score, extracted_info['Montant'], extracted_info['Duree'], monthly_income, monthly_expenses)
        else :
            print("This person is not a customer of our bank and, therefore, is not solvable.")
            return 1;
        
        # Appelez la méthode evaluate_property de PropertyEvaluationService (Belkis)
        is_good_property = client.service.evaluate_property('60101')
        
        print(is_good_property)
        
        # Appelez la méthode verify_solvency de SolvencyVerificationService (Rayan)
    
        return is_good_property 
    
        
    def read_file_to_string(self, file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            print(f"Le fichier '{file_path}' n'a pas été trouvé.")
            return None
        except Exception as e:
            print(f"Une erreur s'est produite lors de la lecture du fichier : {str(e)}")
            return None

# Créez une application Spyne pour coordonner les services
application = Application([_loanService],
    tns='http://localhost/loan-service',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    wsgi_app = WsgiApplication(application)
    
    twisted_apps = [
        (wsgi_app, b'loan-service'),
    ]

    sys.exit(run_twisted(twisted_apps, 8081))
    
    
    
    
    

        
        


