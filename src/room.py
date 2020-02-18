# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    '''
    Room class with attributes: name, description
    '''
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []
    
    def grab_item(self, items):
        self.items.append(item)

    def __str__(self):
        a = ''
        for i, c in enumerate(self.items):
            a += f"{i+1}:{c.name}" 
        return f'{self.name}, {self.description} You will find this item: {self.items}'

    


