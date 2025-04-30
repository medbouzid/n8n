import unittest

# Minimal Item class for testing
class Item:
    def __init__(self, name):
        self.name = name

from your_module import Room  # replace 'your_module' with actual module name

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Hall", "A large wide hall.")
        self.item1 = Item("Sword")
        self.item2 = Item("Shield")
        self.other_room = Room("Kitchen", "A small kitchen.")

    def test_initialization(self):
        self.assertEqual(self.room.name, "Hall")
        self.assertEqual(self.room.description, "A large wide hall.")
        self.assertEqual(self.room.exits, {})
        self.assertEqual(self.room.items, [])

    def test_connect(self):
        self.room.connect(self.other_room, "north")
        self.assertIn("north", self.room.exits)
        self.assertIs(self.room.exits["north"], self.other_room)

    def test_add_item(self):
        self.room.add_item(self.item1)
        self.assertIn(self.item1, self.room.items)

    def test_remove_item(self):
        self.room.add_item(self.item1)
        removed = self.room.remove_item("Sword")
        self.assertEqual(removed, self.item1)
        self.assertNotIn(self.item1, self.room.items)
        # Removing non-existent item returns None
        self.assertIsNone(self.room.remove_item("Potion"))

    def test_remove_item_case_insensitive(self):
        self.room.add_item(self.item1)
        removed = self.room.remove_item("sWoRd")
        self.assertEqual(removed, self.item1)

    def test_get_details_no_items(self):
        self.room.connect(self.other_room, "east")
        details = self.room.get_details()
        self.assertIn("Hall", details)
        self.assertIn("A large wide hall.", details)
        self.assertIn("Exits: east", details)
        self.assertNotIn("You see:", details)

    def test_get_details_with_items(self):
        self.room.add_item(self.item1)
        self.room.add_item(self.item2)
        details = self.room.get_details()
        self.assertIn("You see: Sword, Shield", details)

if __name__ == '__main__':
    unittest.main()