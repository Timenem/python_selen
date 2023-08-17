class Menu:
    def __init__(self, items):
        self.items = items
        self.cursor = 0

    def display(self):
        display_items = [[f"{item}"] if index == self.cursor else str(item) for index, item in enumerate(self.items)]
        return str(display_items)

    def to_the_right(self):
        self.cursor = (self.cursor + 1) % len(self.items)

    def to_the_left(self):
        self.cursor = (self.cursor - 1) % len(self.items)
