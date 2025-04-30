import unittest

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

class TestItem(unittest.TestCase):
    def test_item_init(self):
        item = Item("Apple", "A juicy red fruit")
        self.assertEqual(item.name, "Apple")
        self.assertEqual(item.description, "A juicy red fruit")
    
    def test_item_str(self):
        item = Item("Banana", "A yellow fruit")
        self.assertEqual(str(item), "Banana")

if __name__ == "__main__":
    unittest.main()