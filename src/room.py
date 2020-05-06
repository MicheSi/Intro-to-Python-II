# Implement a class to hold room information. This should have name and
# description attributes.

class Room(Item):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        super().__init__(name, description)
    
    def __str__(self):
        return f'{self.name}: {self.description}'