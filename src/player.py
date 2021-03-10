# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room="undetermined", items_here=[]):
        self.name = name
        self.current_room = current_room
        self.items_here = items_here

    def move(self, direction):
        attribute = direction + '_to'
        if hasattr(self.current_room, attribute):
            self.current_room = getattr(self.current_room, attribute)
        else:
            print("You cannot go in that direction")

    def add_item(self, thing):
        self.items_here.append(thing)

    def drop_item(self, thing):
        self.items_here.remove(thing)

    def __str__(self):
        output = f"\n{self.name}'s current location is {self.current_room} \n and {self.name} is carrying:  "
        for item in self.items_here:
            output += f"{item}, "
        return output

    def __repr__(self):
        return f'Player("{self.name}, {self.current_room}, {self.items_here}")'
