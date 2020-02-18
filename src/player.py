# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item

class Player:
    '''
    Player class with attributes: name, current_room
    '''
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
    
    def __repr__(self):
        return (f"Player(repr{self.name})")

    def __str__(self):
        return f"{self.name}, your current location is: {self.current_room}"

    def move(self, direction):
        str = f"{direction}_to"
        destination = getattr(self.current_room, str)
        if destination:
            self.current_room = destination
        else:
            print("There is no room in that direction.")
    
    def grab_item(self, item):
        self.items.append(item)
        # test = Item(item, "flashlight")
        # test.grab()

    def drop_item(self, item):
        for i in self.items:
            if i.name == name:
                self.items.remove(i)
