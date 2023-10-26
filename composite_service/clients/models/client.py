from enum import Enum
from datetime import datetime

class Client:
    def __init__(self, client_id, balance, red_transactions, current_loans, late_payments):
        self.client_id = client_id
        self.transactions = [] # last 12 months only
        self.balance = balance
        self.current_loans = current_loans
        self.red_transactions = red_transactions
        self.late_payments = late_payments #number of current late payments

class TransactionType(Enum):
    NORMAL = 'Normal'
    SALARY = 'Salary'
    EXPENSE = 'Expense'

class Transaction:
    def __init__(self, client_id, amount, transaction_type, description, date):
        self.client_id = client_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description
        self.date = date