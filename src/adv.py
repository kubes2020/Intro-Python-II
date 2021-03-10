from room import Room
from player import Player
from item import Item

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

# Items Available
item = {
    'fork': Item("fork", """- a metal tool used for eating"""),
    'sword': Item("sword", """- a metal tool used for protection and hunting"""),
    'bucket': Item("bucket", """- a tool used for carrying items"""),
    'lighter': Item("lighter", """- a tool to make fire""")
}

# Add Items to a Room

room['outside'].add_item(item['bucket'])


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player("Brian", room['outside'])

directions = ['n', 's', 'e', 'w']

# this function parses the user's input and either 'get's or 'drop's an item


def parse_command(command):
    words = command.split()
    if words[0] == 'get':
        return player1.add_item(item[words[1]])
    elif words[0] == 'drop':
        return player1.drop_item(item[words[1]])


# Write a loop that:
command = ""
while command != "Q":
    # * Prints the current room name
    print(f"\n{player1.current_room}")
    print("player1 in room", {player1.current_room.name})
# * Prints the current description (the textwrap module might be useful here).

# Prints the current items in Room that are available to pick up
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the command isn't allowed.
# If the user enters "q", quit the game.
    if len(player1.current_room.items_here) > 0:
        command = input(
            "Do you want to pick up an item or drop something you're holding onto? (enter: Y or N)").lower()
        if command == "y":
            command = input(
                "What item? (enter: Get <item name> or Drop <item name>) ")
            parse_command(command)
            print("player1 has", player1)

    command = input(
        "Where do you want to go? (enter: N, S, E, W, or Q to quit): ").lower()
    if command == "q":
        break
    elif command in directions:
        player1.move(command)
    else:
        print("unknown command")
