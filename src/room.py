# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.item = []
    
    def __str__(self):
        return f'{self.name}: {self.description}'

    def add_Item(self, room_Item):
        for i in room_Item:
            self.item.append(i)
    
    def print_Item(self):
        for i in self.item:
            print(i)