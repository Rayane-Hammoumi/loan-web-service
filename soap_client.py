from suds.client import Client


# Remplacez l'URL du service par l'URL de votre service web
service_url = 'http://localhost:8081/loan-service/?wsdl'

# Créez un client SOAP pour le service web
client = Client(service_url)

# Appelez la méthode du service web avec les données appropriées
content = """
            Nom: Smith
            Prenom: John
            Numero Client: 12345
            Duree du pret: 10
            Montant du pret: 10000
          """

# Appelez la méthode extract_information du service TextExtractionService
result = client.service.app_service(content)

if result :
  print("Bonne nouvelle, le pret vous est accorde")
