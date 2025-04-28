class Player:
    def __init__(self, start_room):
        self.current_room = start_room
        self.inventory = []

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            return True
        return False

    def take(self, item_name):
        item = self.current_room.remove_item(item_name)
        if item:
            self.inventory.append(item)
            return item
        return None

    def has_item(self, item_name):
        return any(item.name.lower() == item_name.lower() for item in self.inventory)

    def get_inventory(self):
        if self.inventory:
            return ", ".join(item.name for item in self.inventory)
        return "(empty)"
