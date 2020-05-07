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

#

# Delare all items
items = {
    "Axe": Item('Axe', 'used to chop things'),
    "Matches": Item('Matches', 'used to light a fire'),
    "Candle": Item('Candle', 'used to see in the dark'),
    "Tent": Item('Tent', 'used to sleep and heal player'),
    "Satchel": Item('Satchel', 'now empty, it used to be full of treasure')
}

# Link items to rooms
room['outside'].items = items['Tent']
room['foyer'].items = items['Matches'] 
room['overlook'].items = items['Candle']
room['narrow'].items = items['Axe']
room['treasure'].items = items['Satchel']

# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Player1', room['outside'])

item_list = player.current_room.items
# print(item_list)

# print(player)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while True:
    # print current room name & description
    print(f'\n{player}\n')
    
    print(f'Available items: {item_list}')
    # print(f'Current description: {room[player.current_room].description}')
    # waiting for user input
    move = input('\nSelect a direction to move or type "q" to quit. ')
    # if 'q' is entered, display msg and quit sequence
    if move == 'q':
        print('\nThanks for playing\n')
        break
    # move based on player input
    try:
        if move == 'n':
            if player.current_room.n_to == None:
                print('\nYou cannot go that way!\n')
            else:
                player.move(player.current_room.n_to)

        elif move == 's':
            if player.current_room.s_to == None:
                print('\nYou cannot go that way!\n')
            else:
                player.move(player.current_room.s_to)
        elif move == 'e':
            if player.current_room.e_to == None:
                print('\nYou cannot go that way!\n')
            else:
                player.move(player.current_room.e_to)
        elif move == 'w':
            if player.current_room.w_to == None:
                print('\nYou cannot go that way!\n') 
            else:
                player.move(player.current_room.w_to)
        else:
            print('\nChoose n, s, e or w to move to another room\n')
    except AttributeError:
        print('Choose n, s, e, or w to move to another room')