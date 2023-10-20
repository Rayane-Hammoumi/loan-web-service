import logging
logging.basicConfig(level=logging.DEBUG)
import sys
from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode, AnyDict
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted

import re


class TextExtractionService(ServiceBase) :
    
    @rpc(Unicode, _returns=AnyDict)
    def extract_information(self, loan_application):
            # Define regular expressions for extracting information
        name_pattern = r"Nom: (.+)"
        first_name_pattern = r"Prenom: (.+)"
        customer_number_pattern = r"Numero Client: (.+)"
        loan_duration_pattern = r"Duree du pret: (.+)"
        loan_amount_pattern = r"Montant du pret: (.+)"
        
        # Search for matches in the form
        name_match = re.search(name_pattern, loan_application)
        print(name_match)
        first_name_match = re.search(first_name_pattern, loan_application)
        print(first_name_match)
        customer_number_match = re.search(customer_number_pattern, loan_application)
        print(customer_number_match)
        loan_duration_match = re.search(loan_duration_pattern, loan_application)
        loan_amount_match = re.search(loan_amount_pattern, loan_application)

        # Extract information if matches are found
        if name_match:
            name = name_match.group(1)
        else:
            name = "None"

        if first_name_match:
            first_name = first_name_match.group(1)
        else:
            first_name = "None"

        if loan_duration_match:
            loan_duration = loan_duration_match.group(1)
        else:
            loan_duration = "None"

        if loan_amount_match:
            loan_amount = loan_amount_match.group(1)
        else:
            loan_amount = "None"

        if customer_number_match:
            customer_number = customer_number_match.group(1)
        else:
            customer_number = "None"

        # Return the extracted information
        return {"Nom": name, "Prenom": first_name, "Numero": customer_number,"Duree": loan_duration,  "Montant": loan_amount}
    
