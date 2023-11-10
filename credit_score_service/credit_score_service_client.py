import requests
import sqlite3

# URL des points de terminaison de l'API FastAPI
credit_score_service_endpoint = 'http://127.0.0.1:8000/credit-score'
solvency_verification_service_endpoint = 'http://127.0.0.1:8001/solvency-verification'

# Vos paramètres de client
client_id = 1

# Connectez-vous à la base de données SQLite pour obtenir les données du client
conn = sqlite3.connect('../composite_service/clients/clients.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM clients WHERE client_id = ?", (client_id,))
client_data = cursor.fetchone()

if client_data:
    client_id, balance, red_transactions, current_loans, late_payments = client_data
else:
    print("Client not found")

# Appel à l'API FastAPI pour le score de crédit
credit_score_params = {
    "non_paid_count": red_transactions,
    "current_loans_count": current_loans,
    "late_payments": late_payments
}

response = requests.get(credit_score_service_endpoint, params=credit_score_params)

if response.status_code == 200:
    credit_score = response.json()["credit_score"]
else:
    print(f"Error fetching credit score. Status code: {response.status_code}")
    credit_score = 0  # Valeur par défaut en cas d'erreur

# Appel à l'API FastAPI pour la vérification de la solvabilité
loan_duration = 10
loan_amount = 200000
average_monthly_savings = 1000  # Remplacez cela par votre logique de calcul réelle

solvency_verification_params = {
    "credit_score": credit_score,
    "loan_amount": loan_amount,
    "loan_duration": loan_duration,
    "average_monthly_savings": average_monthly_savings,
    "balance": balance
}

response = requests.get(solvency_verification_service_endpoint, params=solvency_verification_params)

if response.status_code == 200:
    is_solvable = response.json()
else:
    print(f"Error verifying solvency. Status code: {response.status_code}")
    is_solvable = False  # Valeur par défaut en cas d'erreur

# Afficher les résultats
print('client_id: ', client_id)
print('red transactions: ', red_transactions)
print('current loans: ', current_loans)
print('late payments:', late_payments)
print('credit score:', credit_score)
print('loan amount: ', loan_amount)
print('loan_duration: ', loan_duration)
print('is the client solvable ?:', is_solvable)
