import sqlite3
import random

# Connect to the database
conn = sqlite3.connect('property_database.db')
cursor = conn.cursor()

# Create the "properties" table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS properties (
        registration_number TEXT PRIMARY KEY,
        property_type TEXT,
        dimension TEXT,
        price REAL,
        has_garden INTEGER,
        number_of_rooms INTEGER,
        address TEXT,
        dpe TEXT,
        owner TEXT,
        urbanism_compliance INTEGER,
        urbanisme_plan TEXT
    )
''')

# List of possible first names and last names
first_names = ["Martin", "Dupont", "Lefevre", "Dubois", "Robert", "Dufour", "Moreau", "Simon", "Durand", "Lemoine"]
last_names = ["Jean", "Marie", "Pierre", "Paul", "Jacques", "François", "Michel", "Louis", "Henri", "Philippe"]

# List of property types and possible DPE ratings
property_types = ["House", "Apartment", "Mansion"]
dpe_ratings = ["A", "B", "C", "D", "E", "F", "G"]

# Insert 100 properties with random data
for _ in range(100):
    registration_number = str(random.randint(10000, 99999))
    property_type = random.choice(property_types)
    dimension = f"{random.randint(50, 300)}"
    price = random.randint(50000, 1000000)
    has_garden = random.randint(0, 1)
    number_of_rooms = random.randint(1, 10)
    address = f"{random.randint(1, 999)} Main St"
    dpe = random.choice(dpe_ratings)
    owner = f"{random.choice(first_names)} {random.choice(last_names)}"
    urbanism_compliance = random.randint(0, 1)
    urbanisme_plan = random.choice(["PLU", "POS"])

    cursor.execute('''
        INSERT INTO properties 
        (registration_number, property_type, dimension, price, has_garden, number_of_rooms, 
        address, dpe, owner, urbanism_compliance, urbanisme_plan) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (registration_number, property_type, dimension, price, has_garden, number_of_rooms, 
          address, dpe, owner, urbanism_compliance, urbanisme_plan))

# Commit changes and close the connection
conn.commit()
conn.close()
