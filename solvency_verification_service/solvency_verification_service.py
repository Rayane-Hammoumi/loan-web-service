import logging
logging.basicConfig(level=logging.DEBUG)
import sys
from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode, Boolean, Float
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted


class SolvencyVerificationService(ServiceBase):
    @rpc(Integer, Float, Integer, Float, Float, _returns=Boolean)
    def verify_solvency(ctx, credit_score, loan_amount, loan_duration, average_monthly_savings, balance):
        loan_duration_in_months=loan_duration*12
        is_solvable = True
        not_solvable = False
        repayment_per_month = loan_amount / loan_duration / 12

        if credit_score == 0 :
            return not_solvable
        elif balance + (average_monthly_savings - repayment_per_month) * loan_duration_in_months < 0:
            return not_solvable
        else:
            return is_solvable
        
application = Application([SolvencyVerificationService],
    tns='http://localhost/solvency-verification-service',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    wsgi_app = WsgiApplication(application)
    
    twisted_apps = [
        (wsgi_app, b'solvency-verification-service'),
    ]

    sys.exit(run_twisted(twisted_apps, 8078))