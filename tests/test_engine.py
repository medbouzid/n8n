import unittest
from unittest.mock import patch, MagicMock

# Assume the following are available in the same directory as stubs/mocks:
# rooms.py (with class Room), items.py (with class Item), player.py (with class Player)
# and the GameEngine class has been saved in a module named 'game_engine.py'
from game_engine import GameEngine

class TestGameEngine(unittest.TestCase):
    def setUp(self):
        self.engine = GameEngine()

    def test_initial_room(self):
        self.assertEqual(self.engine.player.current_room.name, "Hall")

    def test_create_world_returns_correct_rooms(self):
        rooms = self.engine.create_world()
        for name in ["Hall", "Kitchen", "Bedroom", "Treasure Room"]:
            self.assertIn(name, rooms)
            self.assertIsNotNone(rooms[name])

    def test_handle_command_go_direction(self):
        # Move east from Hall to Bedroom
        self.engine.handle_command("go east")
        self.assertEqual(self.engine.player.current_room.name, "Bedroom")
        # Move west from Bedroom back to Hall
        self.engine.handle_command("go west")
        self.assertEqual(self.engine.player.current_room.name, "Hall")

    def test_handle_command_take_item(self):
        # Move to Bedroom and take Golden Key
        self.engine.handle_command("go east")
        self.engine.handle_command("take golden key")
        self.assertTrue(self.engine.player.has_item("Golden Key"))

    def test_win_condition(self):
        # Move to Bedroom, take Golden Key, then go to Kitchen and Treasure Room
        self.engine.handle_command("go east")
        self.engine.handle_command("take golden key")
        self.engine.handle_command("go west")  # back to Hall
        self.engine.handle_command("go north") # Hall -> Kitchen
        self.engine.handle_command("go east")  # Kitchen -> Treasure Room
        self.assertEqual(self.engine.player.current_room.name, "Treasure Room")
        self.assertTrue(self.engine.player.has_item("Golden Key"))
        # Artificially check_win_condition (normally called via go)
        self.engine.check_win_condition()
        self.assertFalse(self.engine.running)

    def test_help_command_output(self):
        with patch('builtins.print') as mock_print:
            self.engine.handle_command("help")
            mock_print.assert_any_call("Commands:")

    def test_handle_command_inventory_prints(self):
        with patch('builtins.print') as mock_print:
            self.engine.handle_command("inventory")
            mock_print.assert_any_call(f"Inventory: {self.engine.player.get_inventory()}")

    def test_handle_unknown_command(self):
        with patch("builtins.print") as mock_print:
            self.engine.handle_command("xyz")
            mock_print.assert_any_call("I don't understand that command.")

    def test_quit_command_stops_game(self):
        self.assertTrue(self.engine.running)
        with patch("builtins.print"):
            self.engine.handle_command("quit")
        self.assertFalse(self.engine.running)

if __name__ == "__main__":
    unittest.main()