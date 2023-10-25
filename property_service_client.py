import time
import os
from suds.client import Client

service_url = 'http://localhost:8076/loan-service/?wsdl'

# Chemin du répertoire à surveiller (assurez-vous qu'il s'agit du chemin absolu)
directory_to_watch = '/Users/rayanehammoumi/Library/Mobile Documents/com~apple~CloudDocs/Programming/Service/loan-web-service'

# Créez un client SOAP pour le service web
client = Client(service_url)

extracted_info = client.service.evaluate_property('60101')

print(extracted_info)


