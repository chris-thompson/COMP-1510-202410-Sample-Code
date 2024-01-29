"""
Demonstrate how unit test a function that uses random.
Also demonstrates how to mock an object.
"""

from unittest import TestCase
from unittest.mock import patch

from week_06 import roll_die


class TestRollDie(TestCase):

    def test_roll_one_sided_die_once(self):
        expected = 1
        actual = roll_die.roll_die(1, 1)
        self.assertEqual(expected, actual)

    def test_roll_six_sided_die_once(self):
        actual = roll_die.roll_die(1, 6)
        self.assertGreaterEqual(actual, 1)
        self.assertLessEqual(actual, 6)

    def test_roll_six_sided_die_twice(self):
        actual = roll_die.roll_die(2, 6)
        self.assertGreaterEqual(actual, 2)
        self.assertLessEqual(actual, 12)

    def test_roll_ten_sided_die_ten_times(self):
        actual = roll_die.roll_die(10, 10)
        self.assertGreaterEqual(actual, 10)
        self.assertLessEqual(actual, 100)

    @patch('random.randint', side_effect=[5])
    def test_roll_die_single_roll(self, _):
        """
        Wow! Check this out! It's a patch! I am mocking (faking) the random object.
        We call this @patch stuff an annotation. I am annotating the test function.
        We will learn more about this later in the term. When the function we are
        testing (roll_die) is called inside the test function (test_roll_die_single_roll)
        the roll_die function uses random.randint. The @patch is like patching in a
        replacement. The first parameter, random.randint, is the function we are going
        to fake. The second parameter, side_effect, is a list of "pretend" random
        numbers we will "pretend" that randint produces when roll_die uses it.
        Pretty cool, don't you think? You are mocking the random generator so you
        can create a deterministic test, a test where the randomness has been harnessed
        in order to ensure the logic in your function, not randint, is correct!"""
        actual = roll_die.roll_die(3, 3)
        self.assertEqual(actual, 5)

