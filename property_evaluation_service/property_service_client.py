import time
import os
from suds.client import Client

service_url = 'http://localhost:8076/property-service/?wsdl'

# Créez un client SOAP pour le service web
client = Client(service_url)

extracted_info = client.service.evaluate_property('60101')

print(extracted_info)


