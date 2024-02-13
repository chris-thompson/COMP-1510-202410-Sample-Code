"""
Demonstrate how to mock an object.

We are using the patch function from the mock submodule in the unittest module. That's a
mouthful!

We annotate the function the unit test function. That means we write @patch on the line right
before the function. This @patch will do something for us. When the unit test function executes,
the first thing it does is run my_printer. My printer is supposed to print to the console.

But.

We want the printed output to go somewhere permanent so we can test our my_printer function to
make sure it works.

The patch function is decorating the test_my_printer function. It accepts two parameters: the
name of the function we will "mock", and the "thing" we will mock it with.

In this case, when my_printer is called by test_my_printer, it will try to use print. But the
patch will intervene and divert the output to a StringIO object. StringIO is a mutable String type
from the io module. We redirect output to it so that we can then ask it for its value and assert
that our my_printer function did what it was supposed to do!

Note the additional parameter passed to test_my_printer. It's a sensible name for the io.StringIO
object.
"""

from unittest import TestCase
import unittest.mock
import io

import using_a_print_function


class TestMyPrinter(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_my_printer(self, mock_stdout):
        using_a_print_function.my_printer("Hello world!")
        expected = "Hello world!\n"
        self.assertEqual(expected, mock_stdout.getvalue())


