# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    '''
    Player class with attributes: player_name, current_room
    '''
    def __init__(self, player_name, current_room):
        self.player_name = player_name
        self.current_room = current_room
    
    def get_player_name(self):
        '''
        Returns player_name
        '''
        return self.player_name
    
    def get_current_room(self):
        '''
        Returns current_room
        '''
        return self.current_room