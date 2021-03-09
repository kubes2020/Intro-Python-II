# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, in_room="undetermined"):
        self.name = name
        self.in_room = in_room

    def __str__(self):
        output = f"{self.name}'s current location is {self.in_room}"
        return output

    def __repr__(self):
        return f'Player("{self.name}, {self.in_room}")'
