import unittest

class Item:
    def __init__(self, name):
        self.name = name

class Room:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.exits = {}

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for i, item in enumerate(self.items):
            if item.name.lower() == item_name.lower():
                return self.items.pop(i)
        return None

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Room 1")
        self.room2 = Room("Room 2")
        self.room1.exits['north'] = self.room2
        self.room2.exits['south'] = self.room1
        self.key = Item('Key')
        self.room1.add_item(self.key)
        self.player = Player(self.room1)

    def test_initial_room(self):
        self.assertEqual(self.player.current_room, self.room1)

    def test_move_success(self):
        result = self.player.move('north')
        self.assertTrue(result)
        self.assertEqual(self.player.current_room, self.room2)

    def test_move_failure(self):
        result = self.player.move('west')
        self.assertFalse(result)
        self.assertEqual(self.player.current_room, self.room1)

    def test_take_item(self):
        item = self.player.take('Key')
        self.assertIs(item, self.key)
        self.assertIn(self.key, self.player.inventory)
        self.assertNotIn(self.key, self.room1.items)

    def test_take_nonexistent_item(self):
        item = self.player.take('Sword')
        self.assertIsNone(item)

    def test_has_item(self):
        self.assertFalse(self.player.has_item('Key'))
        self.player.take('Key')
        self.assertTrue(self.player.has_item('Key'))
        self.assertTrue(self.player.has_item('key'))  # test case-insensitivity

    def test_get_inventory(self):
        self.assertEqual(self.player.get_inventory(), '(empty)')
        self.player.take('Key')
        self.assertEqual(self.player.get_inventory(), 'Key')

if __name__ == '__main__':
    unittest.main()