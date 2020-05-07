# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room(Item):
    def __init__(self, name, description, item, item_desc):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        super().__init__(item, item_desc)
        self.item = item
    
    def __str__(self):
        return f'{self.name}: {self.description}\nAvailable Items: {self.item} - {self.item_desc}'

    def add_Item(self, *room_Item):
        for i in room_Item:
            self.item.append(i)
    
    def remove_Item(self):
        if i in self.item:
            self.item.remove(i)

    def print_Item(self):
        for i in self.item:
            print(i)