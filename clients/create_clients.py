import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect('clients.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE clients (
        client_id INTEGER PRIMARY KEY,
        balance REAL,
        red_transactions INTEGER,
        current_loans INTEGER,
        late_payments INTEGER
    )
''')

c.execute('''
   CREATE TABLE transactions (
       transaction_id INTEGER PRIMARY KEY,
       client_id INTEGER,
       amount REAL,
       description TEXT,
       date TEXT,
       FOREIGN KEY (client_id) REFERENCES clients(client_id)
   )
''')

# List of phrases for different transaction types
positive_phrases = ["Salaire", "Aide financière", "Remboursement"]
negative_phrases = ["Loisir", "Courses", "Facture"]

# Insert random clients
for id in range(10):
    client_id = id
    balance = random.uniform(-1000, 10000)
    red_transactions = random.choices([0, 0, 0, 0, 1], [0.8, 0.05, 0.05, 0.05, 0.05])[0]
    late_payments = random.choices([0, 0, 1, 1, 1], [0.8, 0.05, 0.05, 0.05, 0.05])[0]
    current_loans = random.randint(0, 2)

    c.execute("INSERT INTO clients (client_id, balance, red_transactions, current_loans, late_payments) VALUES (?, ?, ?, ?, ?)",
              (client_id, balance, red_transactions, current_loans, late_payments))

date_format = "%Y-%m-%d"

for client_id in range(10):
    for _ in range(10):
        amount = random.uniform(-100, 100)
        # Choose a phrase based on the sign of the amount
        if amount >= 0:
            description = random.choice(positive_phrases)
        else:
            description = random.choice(negative_phrases)
        date = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime(date_format)
        c.execute("INSERT INTO transactions (client_id, amount, description, date) VALUES (?, ?, ?, ?)",
                  (client_id, amount, description, date))

# Get today's date
end_date = datetime.today()

# Calculate the start date (16 months ago)
start_date = end_date - timedelta(days=16 * 30)

# Initialize a list to store the first day of each month
dates = []

# Generate the first day of each month
while start_date <= end_date:
    first_day_of_month = start_date.replace(day=1)
    dates.append(first_day_of_month)
    start_date = (first_day_of_month + timedelta(days=32)).replace(day=1)

# Print the list of dates
for client_id in range(10):
    for date in dates:
        amount = random.uniform(1400, 3500)
        if amount >= 0:
            description = random.choice(positive_phrases)
        else:
            description = random.choice(negative_phrases)
        c.execute("INSERT INTO transactions (client_id, amount, description, date) VALUES (?, ?, ?, ?)",
                  (client_id, amount, description, date))

conn.commit()
conn.close()
