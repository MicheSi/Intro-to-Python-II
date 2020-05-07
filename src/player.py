# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f'{self.name} location: {self.current_room}'

    def move(self, room):
        self.current_room = room
    
    def take_item(self, item):
        print(f'Added {item}')
        self.inventory.append(item)

    def drop_item(self, item):
        print(f'Dropped {self.inventory}')
        self.inventory.remove(item)