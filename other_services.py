import logging
logging.basicConfig(level=logging.DEBUG)
import time 
import sys
from spyne import Application, rpc, ServiceBase, Unicode, Integer, Decimal
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted

from property_evaluation_service.property_evaluation_service import PropertyEvaluationService
from Text_Extraction_Service import TextExtractionService

        

# Créez une application Spyne pour coordonner les services
application = Application([TextExtractionService, PropertyEvaluationService],
    tns='http://localhost/other-service',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    wsgi_app = WsgiApplication(application)
    
    twisted_apps = [
        (wsgi_app, b'other-service'),
    ]

    sys.exit(run_twisted(twisted_apps, 8080))

