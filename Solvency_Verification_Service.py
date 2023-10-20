import logging
logging.basicConfig(level=logging.DEBUG)
import sys
from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted


class SolvencyVerificationService(ServiceBase):
    @rpc(Unicode, Unicode, _returns=Unicode)
    def verify_solvency(ctx, credit_score, loan_amount, loan_duration, monthly_income, monthly_expenses):
        loan_duration_in_months=loan_duration*12
        is_solvable = 1
        not_solvable = 0
        repayment_per_month = loan_amount / loan_duration / 12

        if credit_score == 0 :
            return not_solvable
        elif (monthly_income - monthly_expenses - repayment_per_month) * loan_duration_in_months < 0:
            #TODO: ajouter le solde du compte dans la bdd et ici
            return not_solvable
        else:
            return is_solvable