class Item:
    def __init__(self, item, item_desc):
        self.item = item
        self.item_desc = item_desc

    def __str__(self):
        return f'{self.item}: {self.item_desc}'

    def on_take(self):
        print(f'You have picked up {self.item}')

    def on_drop(self):
        print(f'You have dropped {self.item}')
