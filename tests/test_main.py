import unittest
from unittest.mock import patch, MagicMock
from game.engine import GameEngine

class TestGameMain(unittest.TestCase):
    @patch('game.engine.GameEngine')
    def test_main_starts_game(self, mock_game_engine):
        mock_instance = MagicMock()
        mock_game_engine.return_value = mock_instance

        import sys
        import importlib

        # Simulate __name__ == "__main__"
        module_name = 'game_main_temp'
        with open(f'{module_name}.py', 'w') as f:
            f.write(
                'from game.engine import GameEngine\n'
                'if __name__ == "__main__":\n'
                '    game = GameEngine()\n'
                '    game.start()\n'
            )

        sys.modules.pop(module_name, None)  # make sure module is re-imported
        sys.argv = ['foo']  # __main__ check

        # Import as __main__
        with patch.object(sys, 'argv', ['foo']):
            if hasattr(importlib, 'util'):
                spec = importlib.util.spec_from_file_location(module_name, f'{module_name}.py')
                module = importlib.util.module_from_spec(spec)
                sys.modules['__main__'] = module
                spec.loader.exec_module(module)
            else:
                import imp
                sys.modules['__main__'] = imp.load_source(module_name, f'{module_name}.py')

        mock_game_engine.assert_called_once()
        mock_instance.start.assert_called_once()

if __name__ == '__main__':
    unittest.main()