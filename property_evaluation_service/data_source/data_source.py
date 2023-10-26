import sqlite3
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = os.path.dirname(current_dir)
property_module_path = os.path.join(current_dir, 'models')
sys.path.insert(1, property_module_path)

from models.property import Property, PropertyType, EnergyEfficiencyRating, UrbanismPlan

class DataSource:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.conn.close()

    def search_all_properties(self):
        self.cursor.execute('SELECT * FROM properties')
        rows = self.cursor.fetchall()
        return [self.map_row_to_property(row) for row in rows]

    def search_by_registration_number(self, registration_number):
        self.cursor.execute('SELECT * FROM properties WHERE registration_number=?', (registration_number,))
        row = self.cursor.fetchone()
        return self.map_row_to_property(row) if row else None

    def search_similar_addresses(self, address):
        self.cursor.execute('SELECT * FROM properties WHERE address LIKE ?', ('%' + address + '%',))
        rows = self.cursor.fetchall()
        return [self.map_row_to_property(row) for row in rows]
    
    def map_urbanism_plan(self, abbreviation):
        if abbreviation == 'PLU':
            return "Plan Local d'Urbanisme"
        elif abbreviation == 'POS':
            return "Plan d'Occupation des Sols"
        else:
            return None

    def map_row_to_property(self, row):
        if row is None:
            return None
        registration_number, property_type, dimension, price, has_garden, number_of_rooms, address, dpe, owner, urbanism_compliance, urbanisme_plan = row
        urbanism_plan_full_name = self.map_urbanism_plan(urbanisme_plan)
        return Property(registration_number, PropertyType(property_type), dimension, price, bool(has_garden), number_of_rooms, address, EnergyEfficiencyRating(dpe), owner, bool(urbanism_compliance), UrbanismPlan(urbanism_plan_full_name))