# This file is intended only to test if the service is working separately
import time
import os
from suds.client import Client

service_url = 'http://localhost:8080/credit-score-service/?wsdl'

# Créez un client SOAP pour le service web
client = Client(service_url)

credit_score = client.service.calculate_credit_score(1, 2, 10)

print(credit_score)


