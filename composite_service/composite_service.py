import logging
import requests
logging.basicConfig(level=logging.DEBUG)
import time 
import sys
from spyne import Application, rpc, ServiceBase, Unicode, Integer, Decimal, Boolean
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted
import sqlite3
import ast

from suds.client import Client

property_service_endpoint = "http://host.docker.internal:8076/property/evaluate/"
text_extraction_service_endpoint = "http://host.docker.internal:8075/text-extraction-service?wsdl"
credit_score_service_endpoint = "http://host.docker.internal:8077/credit-score-service?wsdl"
solvency_verification_service_endpoint = "http://host.docker.internal:8078/solvency-verification-service?wsdl"

# property_service_endpoint = "http://localhost:8076/property/evaluate/"
# text_extraction_service_endpoint = "http://localhost:8075/text-extraction-service?wsdl"
# credit_score_service_endpoint = "http://localhost:8077/credit-score-service?wsdl"
# solvency_verification_service_endpoint = "http://localhost:8078/solvency-verification-service?wsdl"

class _loanService(ServiceBase):
    
    @rpc(Unicode, _returns=Boolean)
    def app_service(ctx, input_file):
        extracted_info = extract_information(input_file)  
        print("Extracted Info", extracted_info)
        
        client_id = extracted_info['Numero']
        property_reference = extracted_info['Reference']
        loan_amount = extracted_info['Montant']
        
        property_evaluation = check_property_evaluation(property_reference, loan_amount)
        
        is_solvable = check_solvability(client_id)
        
        print("Property Evaluation:", property_evaluation)
        print("Is Solvable:", is_solvable)
            
        return property_evaluation and is_solvable
    
def extract_information(input_file):
    text_extraction_client = Client(text_extraction_service_endpoint)
    # Appelez la méthode extract_information du service TextExtractionService
    extracted_info = text_extraction_client.service.extract_information(input_file)  
    print("Extracted Info", extracted_info)
    return extracted_info

def check_property_evaluation(property_reference, amount):
    url = property_service_endpoint + property_reference
    print("URL :", url)
    response = requests.get(url)
    if response.status_code == 200:
        property_evaluation_data = response.json()
        dpe = property_evaluation_data['compliance']['dpe']
        is_compliant = property_evaluation_data['compliance']['is_compliant']
        avg_prices = property_evaluation_data['average_price']
        print(avg_prices)

        if dpe in ['G', 'F'] and not is_compliant and avg_prices[1] > amount:
            return True
        else:
            return False
        print(extracted_info)
    else:
        print(f"Error: {response.status_code}")
        raise ZeroDivisionError("Error: {response.status_code}")
    
    
def check_solvability(client_id):
    conn = sqlite3.connect('./clients/clients.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients WHERE client_id = ?", (client_id,))
    client_data = cursor.fetchone()
    if client_data:
        client_id, balance, red_transactions, current_loans, late_payments = client_data
    else:
        print("Client not found")
            
    # Testing credit score 
    credit_score_client = Client(credit_score_service_endpoint)
    credit_score = credit_score_client.service.calculate_credit_score(red_transactions, current_loans, late_payments)
            
    cursor.execute("SELECT amount, date FROM transactions WHERE client_id = ? ORDER BY date", (client_id,))
    transactions = cursor.fetchall()

    monthly_savings = {}

    # Go through the transactions
    for amount, date in transactions:
        month_year = date[:7]
        print(month_year)
        print('amount', amount)
        monthly_savings[month_year] = monthly_savings.get(month_year, 0) + amount
        print('Saving for the month {}: '.format(month_year), monthly_savings[month_year])

    # Calculate the average of monthly savings
    total_savings = sum(monthly_savings.values())
    print('total savings: ', total_savings)
    number_of_months = len(monthly_savings)
    print('number of months: ', number_of_months)

    if number_of_months > 0:
        average_monthly_savings = total_savings / number_of_months
    else:
        average_monthly_savings = total_savings #can't divide by 0

    print("\nAverage monthly savings:", average_monthly_savings)

    solvency_verification_client = Client(solvency_verification_service_endpoint)
    loan_duration=10
    loan_amount=200000
    is_solvable = solvency_verification_client.service.verify_solvency(credit_score, loan_amount, loan_duration, average_monthly_savings, balance)
    print('client_id: ', client_id)
    print('red transactions: ', red_transactions)
    print('current loans: ', current_loans)
    print('late payments:', late_payments)
    print('credit score:', credit_score)
    print('loan amount: ', loan_amount)
    print('loan_duration: ', loan_duration)
    print('is the client solvable ?:', is_solvable)
    return is_solvable
    
    
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

    sys.exit(run_twisted(twisted_apps, 8080))