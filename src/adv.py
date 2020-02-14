from room import Room
from player import Player
from item import Item
# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Axe", "A sharp tool that allows you to find resources")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Dagger", "A small sharp tool that allows you to fight your enemies")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Sword", "Sharp tool that allows you to fight off your enemies")]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
# print(room["outside"].n_to)
# Make a new player object that is currently in the 'outside' room.
name= input("enter name: ")
player = Player(room["outside"], name)

print(f"Hello, {player.p_name}")
# Write a loop that:
   
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # print(new_player.p_current_room)

# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print(player.p_current_room)
while True:
    command = input("--> ").lower()
    print(command)
    if command in ["n", "s", "e", "w"]:
        player.move_player(command)
        for item in player.p_current_room: # loops through items that are in a player room
            print(item) # prints out the items in a room
    elif command == "p": # when user clicks "p" player will pick up item
        player.player_item(command) # acess function that allows player to hold item 

    elif command == "d": # when user click "d" player will drop item
        player.item_drop(command) # acesx function that allows player to drop item

    elif command == "q":
        print("Goodbye!")
        exit()
    else:
        print("I do not understand that command")