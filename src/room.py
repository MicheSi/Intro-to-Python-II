# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items
    
    def __str__(self):
        return f'{self.name}: {self.description}'

    def add_Item(self, item, description)
        self.items.append(Item(item, description))
    
    def print_Item(self):
        for i in self.items:
            print(i)