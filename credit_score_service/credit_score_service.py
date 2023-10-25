import logging
logging.basicConfig(level=logging.DEBUG)
import sys
from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted

class Credit_score_service(ServiceBase):
    @rpc(Unicode, Unicode, Unicode, _returns=Unicode)
    def calculate_credit_score(ctx, non_paid_count, current_loans_count, late_payments_count):
        # Assign points for each factor
        credit_score=40
        non_paid_points = -20  # Deduct points for each non-paid instance
        current_loans_points = -10  # Deduct points for each current loan
        late_payments_points = -30  # Deduct points for each late payment

        # Calculate the total credit score
        total_score = (non_paid_count * non_paid_points) + (current_loans_count * current_loans_points) + (late_payments_count * late_payments_points)

        # Cap the minimum score at 0
        if total_score < 0:
            total_score = 0

        return total_score