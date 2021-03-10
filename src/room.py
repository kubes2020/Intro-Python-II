# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items_here=[]):
        self.name = name
        self.description = description
        self.items_here = items_here

    def add_item(self, thing):
        self.items_here.append(thing)

    def __str__(self):
        output = f"{self.name}, is {self.description},\n on display is:  "
        if len(self.items_here) > 0:
            for item in self.items_here:
                output += f"{item}, "
        else:
            output += "no items"

        return output
