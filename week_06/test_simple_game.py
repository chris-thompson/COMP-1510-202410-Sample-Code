"""
More unit testing. Three patches.

We can patch input( ) using builtins.input. We pass it side_effects in a list.

We can patch random.randint( ) by generating a deterministic return_value.

We can redirect output from stdout to a StringIO object which is a new_callable because we can call
upon it to tell us information about what it stores.

Note that we have to assign names to all the mock objects even when the mock objects are
not explicitly used inside the test function. You can tell they aren't because their names are
grey instead of white, like mock_output, the io.StringIO object, which is called upon directly
in the test function's code.
"""

import io
from unittest import TestCase
from unittest.mock import patch

from week_06.simple_game import simple_game


class TestSimpleGame(TestCase):

    @patch('builtins.input', side_effect=[1, 10, 5])
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_simple_game(self, mock_output, _, __):
        simple_game()
        the_game_printed_this = mock_output.getvalue()
        expected_output = "You're right!\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[1, 10, 5])
    @patch('random.randint', return_value=6)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_simple_game_too_low(self, mock_output, _, __):
        simple_game()
        the_game_printed_this = mock_output.getvalue()
        expected_output = "Too low, the number was 6\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[1, 10, 5])
    @patch('random.randint', return_value=4)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_simple_game_too_high(self, mock_output, _, __):
        simple_game()
        the_game_printed_this = mock_output.getvalue()
        expected_output = "Too high, the number was 4\n"
        self.assertEqual(expected_output, the_game_printed_this)

