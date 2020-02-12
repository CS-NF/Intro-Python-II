# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, p_starting_room, p_name):
        self.p_current_room = p_starting_room
        self.p_name = p_name


    # function that will allow the player to move from room to room
    def move_plater(self, direction):
        next_room = self.p_current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.p_current_room = next
            print(self.p_current_room)
        else:
            print("You cannot move in that direction")
        