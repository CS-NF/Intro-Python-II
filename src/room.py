# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, room_name, description):
        self.room_name = room_name
        self.description = description
        self.n_to = None
        self.s_to = None 
        self.e_to = None 
        self.w_to = None 
        self.items = []

    def __str__(self):
        return f"{self.room_name} is {self.description}"

    def room_direction(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None 

    def inventory(self, inventory_items):

        malay_weapons = ["Sword", "Axe", "Dagger"]
        long_range_weapons = ["Crossbow", "Slingshot", "Throwing axe"]
        weak_weapons = ["rock", "stick"]

        if inventory_items == self.n_to:
            return self.items.append(malay_weapons)
        elif inventory_items == self.s_to:
            return self.items.append(long_range_weapons)
        elif inventory_items == self.e_to:
            return self.items.append(malay_weapons)
        elif inventory_items == self.w_to:
            return self.items.append(weak_weapons)