# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, p_starting_room, p_name):
        self.p_current_room = p_starting_room
        self.p_name = p_name
        self.items = []
         

    # function that will allow the player to move from room to room
    def move_player(self, direction):
        next_room = self.p_current_room.room_direction(direction)
        if next_room is not None:
            self.p_current_room = next_room
            print(self.p_current_room)
        else:
            print("You cannot move in that direction")
        
# allows player to hold an item
    def player_item(self, item):
        self.items.append(item)
        print(f"{item} has been picked up")

    # function that will allow the player to drop an item 
    def item_drop(self, item):
        self.items.remove(item)
        print(f"{item} has been droped")