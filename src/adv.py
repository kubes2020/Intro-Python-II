from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# Make a new player object that is currently in the 'outside' room.
player1 = Player("Brian", room['outside'])
# print(room['outside'])
# print(player1.in_room)
# print(player1)


# Write a loop that:
movement = ""
while movement != "Q":
    # * Prints the current room name
    print(f"\nCurrent location: {player1.in_room.name}")
# * Prints the current description (the textwrap module might be useful here).
    print(f"description: {player1.in_room.description}")
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    movement = input(
        "Where do you want to go? (enter: N, S, E, W, or Q to quit): ").upper()
    if movement == "Q":
        break
    elif movement == "N":
        try:
            player1.in_room.n_to
            player1.in_room = player1.in_room.n_to
        except:
            print("You cannot go there")
    elif movement == "S":
        try:
            player1.in_room.s_to
            player1.in_room = player1.in_room.s_to
        except:
            print("You cannot go there")
    elif movement == "E":
        try:
            player1.in_room.e_to
            player1.in_room = player1.in_room.e_to
        except:
            print("You cannot go there")
    elif movement == "W":
        try:
            player1.in_room.w_to
            player1.in_room = player1.in_room.w_to
        except:
            print("You cannot go there")
