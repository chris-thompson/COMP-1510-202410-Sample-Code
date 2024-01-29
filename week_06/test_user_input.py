from unittest import TestCase
from unittest.mock import patch

from week_06 import user_input

"""
Demonstrate how to mock an object.

This is how we can test user input.

We "mock" it! We create a "mock" object that we can
"program" to act as the input stream. When the function
we are unit testing calls builtins.input, we intervene so
the unit test doesn't actually let our function call input.
Instead we say, oh, no, use this "fake" input that I will 
patch into the test. And here is the string you will
pretend I just input.
"""


class TestAskForValueAndConvertToLower(TestCase):

    @patch('builtins.input', side_effect=['2qt4wrdz'])
    def test_ask_for_value_and_convert_to_upper(self, _):
        actual = user_input.ask_for_value_and_convert_to_upper()
        expected = "2QT4WRDZ"
        self.assertEqual(expected, actual)

