import logging
logging.basicConfig(level=logging.DEBUG)
import sys
from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.util.wsgi_wrapper import run_twisted


# class SolvencyVerificationService(ServiceBase):
#     @rpc(Unicode, Unicode, _returns=Unicode)
#     def verify_solvency(ctx, extracted_info):
#         is_solvable = 1
#         not_solvable = 0

#         client_database = {
#             1: {
#                 'client_number': 1,
#                 'monthly_income': 4000,
#                 'account_balance': 1000.0,
#                 'monthly_expenses': 500.0,
#                 'outstanding_loans': 2,
#                 'late_payments': 1,
#                 'times_unpaid': 2
#             },
#             2: {
#                 'client_number': 2,
#                 'monthly_income': 1000,
#                 'account_balance': 1500.0,
#                 'monthly_expenses': 600.0,
#                 'outstanding_loans': 1,
#                 'late_payments': 0,
#                 'times_unpaid': 0
#             },
#             3: {
#                 'client_number': 3,
#                 'monthly_income': 2000,
#                 'account_balance': 2000.0,
#                 'monthly_expenses': 700.0,
#                 'outstanding_loans': 3,
#                 'late_payments': 2,
#                 'times_unpaid': 3
#             }
#         }

#         if extracted_info['client_number'] in client_database:
#             client_info = client_database[extracted_info['client_number']]
#         else:
#             print("Client with ID {extracted_info['client_number']} not found in the database.")
#             return not_solvable

#         repayment_per_month = extracted_info['Amount'] / (extracted_info['Duration'] / 12)

#         if client_info['account_balance'] + ((client_info['monthly_income'] - client_info['monthly_expenses'] - repayment_per_month)) * extracted_info['loan_duration_months'] < 0:
#             return not_solvable
#         elif client_info['times_unpaid'] > 3:
#             return not_solvable
#         elif client_info['outstanding_loans'] >= 1 and client_info['late_payments'] >= 1:
#             return not_solvable
#         else:
#             return is_solvable