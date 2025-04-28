from .items import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}  # direction: Room
        self.items = []

    def connect(self, other_room, direction):
        self.exits[direction] = other_room

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for i, item in enumerate(self.items):
            if item.name.lower() == item_name.lower():
                return self.items.pop(i)
        return None

    def get_details(self):
        info = f"{self.name}\n{self.description}\n"
        if self.items:
            info += "You see: " + ", ".join(item.name for item in self.items) + "\n"
        info += "Exits: " + ", ".join(self.exits.keys()) + "\n"
        return info
