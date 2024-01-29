from unittest import TestCase


class Test(TestCase):
    """
    The easiest way to generate a unit test for a function in PyCharm is to right-click the function
    and select Go To > Test.

    Traditionally we start with a test that fails. That's what this is here. It's like the pass
    statement of the unit test world. We have to put something in the test function. But we haven't
    written any code yet. So start with a test that fails, and then strive to implement a test
    that our tested code can pass.
    """
    def test_function(self):
        self.fail()
