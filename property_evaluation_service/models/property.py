from enum import Enum

# titre de la propriete ca inclut le propriétaire, adresse, et le numéro d'enregistrement

class UrbanismPlan(Enum):
    """
    Enumeration representing the type of urbanism plan.
    """
    PLU = "Plan Local d'Urbanisme"  # Represents Plan Local d'Urbanisme
    POS = "Plan d'Occupation des Sols"  # Represents Plan d'Occupation des Sols

class PropertyType(Enum):
    HOUSE = "House"
    APARTMENT = "Apartment"
    MANSION = "Mansion"

class EnergyEfficiencyRating(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"

class Property:
    def __init__(self, registration_number, property_type, dimension, price, has_garden, number_of_rooms, address, dpe, owner, urbanism_compliance, urbanisme_plan):
        self.registration_number = registration_number
        self.property_type = property_type
        self.dimension = dimension
        self.price = int(price)
        self.has_garden = has_garden
        self.number_of_rooms = number_of_rooms
        self.address = address
        self.dpe = dpe
        self.owner = owner
        self.urbanism_compliance = urbanism_compliance
        self.urbanisme_plan = urbanisme_plan
    def __str__(self):
        return f"Property #{self.registration_number}\n" \
               f"Type: {self.property_type.value}\n" \
               f"Dimension: {self.dimension}\n" \
               f"Price: {self.price}\n" \
               f"Has Garden: {'Yes' if self.has_garden else 'No'}\n" \
               f"Number of Rooms: {self.number_of_rooms}\n" \
               f"Address: {self.address}\n" \
               f"DPE: {self.dpe.value}\n" \
               f"Owner: {self.owner}\n" \
               f"Urbanism Compliance: {'Yes' if self.urbanism_compliance else 'No'}\n" \
               f"Urbanism Plan: {self.urbanisme_plan.value}"
        
