import sqlite3
import random
from datetime import datetime, timedelta
from models.client import Client, TransactionType, Transaction

conn = sqlite3.connect('clients.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE clients (
        client_id INTEGER PRIMARY KEY,
        balance REAL,
        red_transactions INTEGER,
        current_loans INTEGER
    )
''')

c.execute('''
   CREATE TABLE transactions (
       transaction_id INTEGER PRIMARY KEY,
       client_id INTEGER,
       amount REAL,
       transaction_type TEXT,
       description TEXT,
       date TEXT,
       FOREIGN KEY (client_id) REFERENCES clients(client_id)
   )
''')

# Insert random clients
for id in range(10):
    client_id = id
    balance = random.uniform(-1000, 10000)
    red_transactions = random.randint(0, 7)  # Assuming 0 to 10 red transactions
    current_loans = random.randint(0, 2)  # Assuming 0 to 2 current loans

    c.execute("INSERT INTO clients (client_id, balance, red_transactions, current_loans) VALUES (?, ?, ?, ?)",
              (client_id, balance, red_transactions, current_loans))
    
date_format = "%Y-%m-%d"  # Format for date input

for client_id in range(0, 10):
    for _ in range(10):
        transaction_type = random.choice(list(TransactionType))
        if (transaction_type == TransactionType.SALARY):
            continue
        amount = random.uniform(-100, 100)  # Assume transactions can be negative or positive
        description = f'Transaction for client {client_id}'
        date = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime(date_format)
        c.execute("INSERT INTO transactions (client_id, amount, transaction_type, description, date) VALUES (?, ?, ?, ?, ?)",
                  (client_id, amount, transaction_type.value, description, date))

# Get today's date
end_date = datetime.today()

# Calculate the start date (16 months ago)
start_date = end_date - timedelta(days=16*30)  # Assuming 30 days in a month

# Initialize a list to store the first day of each month
dates = []

# Generate the first day of each month
while start_date <= end_date:
    first_day_of_month = start_date.replace(day=1)
    dates.append(first_day_of_month)
    start_date = (first_day_of_month + timedelta(days=32)).replace(day=1)  # Move to next month's first day

# Print the list of dates
for client_id in range(0, 10):
    for date in dates:
        print(date.strftime('%Y-%m-%d'))
        transaction_type = TransactionType.SALARY
        amount = random.uniform(1400, 3500) 
        description = f'Transaction for client {client_id}'
        c.execute("INSERT INTO transactions (client_id, amount, transaction_type, description, date) VALUES (?, ?, ?, ?, ?)",
                  (client_id, amount, transaction_type.value, description, date))

conn.commit()
conn.close()
