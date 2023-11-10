# This file is intended only to test if the service is working separately
import time
import os
from suds.client import Client
import sqlite3

credit_score_service_endpoint = 'http://localhost:8077/credit-score-service/?wsdl'
solvency_verification_service_endpoint = "http://localhost:8078/solvency-verification-service?wsdl"


# Créez un client SOAP pour le service web
client_id = 1
conn = sqlite3.connect('../clients/clients.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM clients WHERE client_id = ?", (client_id,))
client_data = cursor.fetchone()

if client_data:
    client_id, balance, red_transactions, current_loans, late_payments = client_data
else:
    print("Client not found")
        
# Testing credit score 
credit_score_client = Client(credit_score_service_endpoint)
credit_score = credit_score_client.service.calculate_credit_score(red_transactions, current_loans, late_payments)
        
cursor.execute("SELECT amount, date FROM transactions WHERE client_id = ? ORDER BY date", (client_id,))
transactions = cursor.fetchall()

monthly_savings = {}

# Go through the transactions
for amount, date in transactions:
    month_year = date[:7]
    print(month_year)
    print('amount', amount)
    monthly_savings[month_year] = monthly_savings.get(month_year, 0) + amount
    print('Saving for the month {}: '.format(month_year), monthly_savings[month_year])

# Calculate the average of monthly savings
total_savings = sum(monthly_savings.values())
print('total savings: ', total_savings)
number_of_months = len(monthly_savings)
print('number of months: ', number_of_months)

if number_of_months > 0:
    average_monthly_savings = total_savings / number_of_months
else:
    average_monthly_savings = total_savings #can't divide by 0

print("\nAverage monthly savings:", average_monthly_savings)

solvency_verification_client = Client(solvency_verification_service_endpoint)
loan_duration=10
loan_amount=200000
is_solvable = solvency_verification_client.service.verify_solvency(credit_score, loan_amount, loan_duration, average_monthly_savings, balance)
print('client_id: ', client_id)
print('red transactions: ', red_transactions)
print('current loans: ', current_loans)
print('late payments:', late_payments)
print('credit score:', credit_score)
print('loan amount: ', loan_amount)
print('loan_duration: ', loan_duration)
print('is the client solvable ?:', is_solvable)