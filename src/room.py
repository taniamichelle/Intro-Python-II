# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    '''
    Room class with attributes: room_name, description
    '''
    def __init__(self, room_name, description):
        self.room_name = room_name
        self.description = description
    
    def get_room_name(self):
        '''
        Returns room_name
        '''
        return self.room_name
    
    def get_description(self):
        '''
        Returns description
        '''
        return self.description