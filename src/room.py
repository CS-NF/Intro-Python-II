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

    def __str__(self):
        print(f"{self.room_name} is {self.description}")

    def room_direction(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to:
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None