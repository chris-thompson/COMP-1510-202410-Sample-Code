from unittest import TestCase

from week_04.square import square


class Test(TestCase):
    def test_positive_integer(self):
        self.assertEqual(4, square(2))

    def test_negative_integer(self):
        self.assertEqual(4, square(-2))

    def test_zero(self):
        self.assertEqual(0, square(0))

    def test_positive_float(self):
        self.assertEqual(2.25, square(1.5))

    def test_negative_float(self):
        self.assertEqual(2.25, square(-1.5))
