from .rooms import Room
from .items import Item
from .player import Player

class GameEngine:
    def __init__(self):
        self.win_room_name = "Treasure Room"
        self.win_item_name = "Golden Key"
        self.rooms = self.create_world()
        self.player = Player(self.rooms["Hall"])
        self.running = True

    def create_world(self):
        # Rooms
        hall = Room("Hall", "A large hall with marble floors.")
        kitchen = Room("Kitchen", "A kitchen with dusty utensils.")
        bedroom = Room("Bedroom", "A quiet bedroom. There's something under the bed.")
        treasure_room = Room("Treasure Room", "A room glittering with gold!")

        # Connections
        hall.connect(kitchen, "north")
        kitchen.connect(hall, "south")
        hall.connect(bedroom, "east")
        bedroom.connect(hall, "west")
        kitchen.connect(treasure_room, "east")
        treasure_room.connect(kitchen, "west")

        # Items
        golden_key = Item("Golden Key", "A shiny key that looks valuable.")
        bedroom.add_item(golden_key)
        kitchen.add_item(Item("Apple", "A fresh-looking apple."))

        return {
            "Hall": hall,
            "Kitchen": kitchen,
            "Bedroom": bedroom,
            "Treasure Room": treasure_room
        }

    def start(self):
        print("Welcome to the Text Adventure Game!")
        print("Type 'help' for commands.")
        while self.running:
            print("\n" + self.player.current_room.get_details())
            command = input("> ").strip().lower()
            self.handle_command(command)

    def handle_command(self, command):
        if command in ["quit", "exit"]:
            print("Goodbye!")
            self.running = False
        elif command in ["help", "h"]:
            self.print_help()
        elif command.startswith("go "):
            direction = command[3:]
            if self.player.move(direction):
                print(f"You move {direction}.")
                self.check_win_condition()
            else:
                print(f"You can't go '{direction}'.")
        elif command.startswith("take "):
            item_name = command[5:]
            item = self.player.take(item_name)
            if item:
                print(f"You picked up {item.name}.")
            else:
                print(f"There's no '{item_name}' here.")
        elif command in ["inventory", "inv"]:
            print(f"Inventory: {self.player.get_inventory()}")
        else:
            print("I don't understand that command.")

    def print_help(self):
        print("Commands:")
        print("  go [direction]   -- Move north, south, east, west")
        print("  take [item]      -- Pick up an item")
        print("  inventory / inv  -- Show your inventory")
        print("  help             -- Show this help message")
        print("  quit / exit      -- Quit the game")

    def check_win_condition(self):
        if (self.player.current_room.name == self.win_room_name and
                self.player.has_item(self.win_item_name)):
            print("\nCongratulations! You used the Golden Key to enter the Treasure Room and win!")
            self.running = False
