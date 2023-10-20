import sqlite3

class BankDatabase:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()
        self.create_clients_table()

    def create_clients_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY,
                nom TEXT NOT NULL,
                revenu_mensuel REAL,
                depenses_mensuelles REAL,
                faillite BOOLEAN,
                paiements_en_retard INTEGER
            )
        ''')
        self.conn.commit()

    def close(self):
        self.conn.close()
    def get_client_by_id(self, client_id):
        self.cursor.execute("SELECT * FROM clients WHERE id = ?", (client_id,))
        client_data = self.cursor.fetchone()
        return client_data

if __name__ == "__main__":
    # Example of how to use the ClientDatabase class
    db = BankDatabase('client_database.db')

    # You can perform operations using the database

    # Ajout d'un client
    db.cursor.execute("INSERT INTO clients (id, nom, revenu_mensuel, depenses_mensuelles, faillite, paiements_en_retard) VALUES (?,?, ?, ?, ?, ?)",
               (1,"John Doe", 5000.0, 3000.0, 0, 2))
    db.cursor.execute("INSERT INTO clients (id, nom, revenu_mensuel, depenses_mensuelles, faillite, paiements_en_retard) VALUES (?,?, ?, ?, ?, ?)",
               (2,"Silvain Doe", 100000.0, 35000.0, 1, 3))
    # Get a client's information by their ID
    client_id_to_retrieve = 2  # Replace with the ID of the client you want to retrieve
    client_data = db.get_client_by_id(client_id_to_retrieve)

    if client_data:
        print("Client Information:")
        print(f"ID: {client_data[0]}")
        print(f"Nom: {client_data[1]}")
        print(f"Revenu Mensuel: {client_data[2]}")
        print(f"Depenses Mensuelles: {client_data[3]}")
        print(f"Faillite: {client_data[4]}")
        print(f"Paiements en Retard: {client_data[5]}")
    else:
        print("Client not found or an error occurred.")

    # Close the database connection when done
    db.close()
