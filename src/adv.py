from room import Room
from player import Player
from item import Item

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons."),

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

# Make a new player object(or instance of Player) that is currently in the 'outside' room.  
p1 = Player("One", room["outside"])
print(p1.name)

# Make a new item object(or instance of Item)  
i1 = Item("rope", "You have found a rope!")
i2 = Item("flashlight", "You have found a flashlight!")
i3 = Item("stick", "You have found a stick!")
i4 = Item("blanket", "You have found a blanket!")
i5 = Item("snack", "You have found a snack!")

print(i1.name)

room["outside"].items.append(i1)
room["foyer"].items.append(i2)
room["overlook"].items.append(i3)
room["narrow"].items.append(i4)
room["treasure"].items.append(i5)

directions = ['n', 'e', 's', 'w']
actions = ['grab', 'drop']

# LOOP 
while True: 
    
    # READ
    print(p1)
    cmd = input("Please enter a command: ").split(" ")
    current_room = p1.current_room
    if len(cmd) > 1:
        item_interest = cmd[1]
        cmd = cmd[0]
    elif len(cmd) == 1:
        cmd = cmd[0]

    # EVAL    
    if cmd in directions:
        p1.move(cmd)
        # print(f"testing {p1.current_room.items}")
    elif cmd in actions:
        if cmd == 'grab':
            p1.grab_item(item)
            print("Items: ", p1.items)
            for item in p1.items:
                print(item)
        elif cmd == 'drop':
            pass
    elif cmd == 'q':
        print("Goodbye!")
        break
    else:
        print("Please enter a valid command.")


    # If the user enters a cardinal direction, attempt to move to the room there.
    # if cmd == "n":
    #     try:
    #         if p1.current_room == "Outside":
    #             # Prints the current room name
    #             print(f"{p1.name}, your current location is: {p1.current_room}.")
    #             # Prints the current description (the textwrap module might be useful here).
    #             pass
    #         elif p1.current_room == "Foyer":
    #             current_room = current_room.n_to
    #             print(f"{p1.name}, your current location is: {p1.current_room}.")
    #         elif p1.current_room == "Narrow":
    #             current_room = current_room.n_to
    #             print(f"{p1.name}, your current location is: {p1.current_room}.")
    #         # Print an error message if the movement isn't allowed.
    #     except:
    #         print(f"{cmd} is not allowed here.")
    # elif cmd == "e":
    #     try:
    #         if p1.current_room == "Narrow":
    #             current_room = current_room.e_to
    #             print(f"{p1.name}, your current location is: {p1.current_room}.")
    #     except:
    #         print(f"{cmd} is not allowed here.")
    # elif cmd == "s":
    #     try:
    #         if p1.current_room == "Overlook":
    #             current_room = current_room.s_to
    #             print(f"{p1.name}, your current location is: {p1.current_room}.")
    #         elif p1.current_room == "Foyer":
    #             current_room = current_room.s_to
    #             print(f"{p1.name}, your current location is: {p1.current_room}.")
    #         elif p1.current_room == "Treasure":
    #             current_room = current_room.s_to
    #             print(f"{p1.name}, your current location is: {p1.current_room}.")
    #     except:
    #         print(f"{cmd} is not allowed here.")
    # elif cmd == "w":
    #     try:
    #         if p1.current_room == "Foyer":
    #             current_room = current_room.w_to
    #             print(f"{p1.name}, your current location is: {p1.current_room}.")
    #     except:
    #         print(f"{cmd} is not allowed here.")
    # # else cmd == "q":
    # #     try:
    # #     print("Goodbye!")
    # #     # If the user enters "q", quit the game.
