import logging
logging.basicConfig(level=logging.DEBUG)
import sys
from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted

class Credit_Score_Service(ServiceBase):
    @rpc(Integer, Integer, Integer, _returns=Integer)
    def calculate_credit_score(self, non_paid_count, current_loans_count, late_payments):
        # Assign points for each factor
        credit_score=40
        non_paid_points = -20  # Deduct points for each non-paid instance
        current_loans_points = -10  # Deduct points for each current loan
        late_payments_points = -30  # Deduct points for each late payment

        # Calculate the total credit score
        credit_score = credit_score + (non_paid_count * non_paid_points) + (current_loans_count * current_loans_points) + (late_payments * late_payments_points)
    
        # Cap the minimum score at 0
        if credit_score < 0:
            credit_score = 0

        print(f"Total Score: {credit_score}")
        return credit_score


application = Application([Credit_Score_Service],
    tns='http://localhost/credit-score-service',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    wsgi_app = WsgiApplication(application)
    
    twisted_apps = [
        (wsgi_app, b'credit-score-service'),
    ]

    sys.exit(run_twisted(twisted_apps, 8080))
    