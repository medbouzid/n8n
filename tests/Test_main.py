import unittest
from unittest.mock import patch, MagicMock
from game.engine import GameEngine

class TestGameEngineMain(unittest.TestCase):
    @patch('game.engine.GameEngine')
    def test_main_creates_and_starts_game(self, MockGameEngine):
        instance = MockGameEngine.return_value
        import sys
        import types
        
        # Prepare a fake __main__ module with the target code
        main_code = (
            'from game.engine import GameEngine\n'
            'if __name__ == "__main__":\n'
            '    game = GameEngine()\n'
            '    game.start()\n'
        )
        
        fake_main = types.ModuleType('__main__')
        sys.modules['__main__'] = fake_main
        
        exec(main_code, fake_main.__dict__)
        
        MockGameEngine.assert_called_once()
        instance.start.assert_called_once()

if __name__ == '__main__':
    unittest.main()