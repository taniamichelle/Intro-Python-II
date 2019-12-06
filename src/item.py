class Item:
    '''
    Item class with attributes: name and description
    '''
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __repr__(self):
        return f"Item({repr(self.name)})"
    
    def __str__(self):
        return f"{self.name}"

    def grab(self):
        print(f"You have picked up: {self.name}")
    
    def drop(self):
        print(f"You have dropped: {self.name}")