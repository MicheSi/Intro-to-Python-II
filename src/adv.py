from room import Room
from player import Player

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
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Player1', room['outside'])

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
    print(f'\n{player.current_room}\n')
    # print(f'Current description: {room[player.current_room].description}')
    # waiting for user input
    move = input('Select a direction to move or type "q" to quit.')
    # if 'q' is entered, display msg and quit sequence
    if move == 'q':
        print('Thanks for playing')
        break
    # move based on player input
    try:
        if move == 'n':
            if player.current_room.n_to == None:
                print('\nYou cannot go that way!\n')
                player.move(player.s_to)
            else:
                player.move(player.current_room.n_to)
        if move == 's':
            if player.current_room.s_to == None:
                print('You cannot go that way!')
            else:
                player.move(player.current_room.s_to)
        if move == 'e':
            if player.current_room.e_to == None:
                print('You cannot go that way!')
            else:
                player.move(player.current_room.e_to)
        if move == 'w':
            if player.current_room == None:
                print('You cannot go that way!')
            else:
                player.move(player.current_room.w_to)
    except AttributeError:
        print('Choose n, s, e, or w to move to another room')