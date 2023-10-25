import logging
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted

logging.basicConfig(level=logging.DEBUG)

class SolvencyVerificationService(ServiceBase):
    @rpc(Unicode, Unicode, Unicode, Unicode, Unicode, _returns=Unicode)
    def verify_solvency(ctx, credit_score, loan_amount, loan_duration, monthly_income, monthly_expenses):
        loan_duration_in_months = int(loan_duration) * 12
        is_solvable = "1"
        not_solvable = "0"
        repayment_per_month = float(loan_amount) / int(loan_duration) / 12

        if credit_score == "0":
            return not_solvable
        elif (int(monthly_income) - int(monthly_expenses) - repayment_per_month) * loan_duration_in_months < 0:
            return not_solvable
        else:
            return is_solvable

application = Application([SolvencyVerificationService], 'your_namespace',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    wsgi_application = WsgiApplication(application)

    server = make_server('0.0.0.0', 8000, wsgi_application)
    server.serve_forever()
