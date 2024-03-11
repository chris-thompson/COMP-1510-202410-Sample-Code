from unittest import TestCase
from cat import Cat


class TestCat(TestCase):

    def setUp(self):
        self.test_cat = Cat("Bubba", 3)

    def test_get_name(self):
        expected = "Bubba"
        actual = self.test_cat.get_name()
        self.assertEqual(expected, actual)

    def test_get_age(self):
        expected = 3
        actual = self.test_cat.get_age()
        self.assertEqual(expected, actual)
