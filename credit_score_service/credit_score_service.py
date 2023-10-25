import logging
logging.basicConfig(level=logging.DEBUG)
import sys
from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted

def calculate_credit_score(cx, non_paid_count, current_loans_count, late_payments_count):
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






























def calculate_credit_score(delinquencies, open_credit_lines, current_late_payments, salary, account_balance):
    # Apply weights to different features based on their importance
    weight_delinquencies = 0.3
    weight_open_credit_lines = 0.2
    weight_current_late_payments = 0.2
    weight_salary = 0.1
    weight_account_balance = 0.2

    # Calculate the score using a simple formula
    credit_score = (
        weight_delinquencies * delinquencies +
        weight_open_credit_lines * open_credit_lines +
        weight_current_late_payments * current_late_payments +
        weight_salary * salary +
        weight_account_balance * account_balance
    )

    return credit_score

def decide_loan_approval(credit_score, loan_amount, loan_duration):
    # Define your own decision criteria for loan approval here
    minimum_score = 700
    maximum_loan_amount = 50000
    maximum_loan_duration = 60

    if (credit_score >= minimum_score) and (loan_amount <= maximum_loan_amount) and (loan_duration <= maximum_loan_duration):
        return "The loan is approved."
    else:
        return "The loan is denied."

# Example usage
delinquencies = 2
open_credit_lines = 1
current_late_payments = 0
salary = 50000
account_balance = 10000

credit_score = calculate_credit_score(delinquencies, open_credit_lines, current_late_payments, salary, account_balance)
decision = decide_loan_approval(credit_score, loan_amount=20000, loan_duration=48)

print(f"Credit Score: {credit_score}")
print(f"Loan Approval Decision: {decision}")
