import time
import os
from suds.client import Client

# URL du service web
service_url = 'http://localhost:8081/loan-service/?wsdl'

current_path = os.getcwd()
file_path = os.path.join(current_path, 'test.txt')

client = Client(service_url)

with open(file_path, 'r') as file:
    file_contents = file.read()
    print(file_contents)
    extracted_info = client.service.app_service(file_contents)        
    if extracted_info :
        print("Bonne nouvelle, le pret vous est accorde")
    else :
        print("Malheureusement, le pret ne pourrait pas vous etre accorde")