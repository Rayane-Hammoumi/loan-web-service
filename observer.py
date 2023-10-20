import time
import os
from suds.client import Client

# URL du service web
service_url = 'http://localhost:8081/loan-service/?wsdl'

# Chemin du répertoire à surveiller (assurez-vous qu'il s'agit du chemin absolu)
# Créez un client SOAP pour le service web
client = Client(service_url)

with open('/Users/h.hidouri/Downloads/myenv 2/test.txt', 'r') as file:
    file_contents = file.read()
    print(file_contents)
    extracted_info = client.service.app_service(file_contents)        
    if extracted_info :
        print("Bonne nouvelle, le pret vous est accorde")

