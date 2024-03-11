"""
A module for demonstrating exceptions.

Use common or existing exceptions when possible, i.e.:

IndexError
KeyError
ValueError
TypeError
etc.

Examine the following functions. They all do the same thing, more or less. But as we travel
down the list, the quality of the function increases.

What change(s) do you observe from convert to another_convert to yet_another_convert to
informative_convert?

"""

import sys


def a_terrible_non_pythonic_convert_dont_do_this(positive_integer):
    """
    This code is not Pythonic. Yuck. Who wrote this, a Java developer?
    """
    if positive_integer < 0:
        raise ValueError("No negative numbers!")
    if not isinstance(positive_integer, int):
        raise TypeError("That's not an integer")


def convert(value):
    """
    Convert to an integer.  Meh. This is just Meh. That -1 stuff tells me a C developer wrote this.
    """
    try:
        the_int = int(value)
    except ValueError:
        the_int = -1
    return the_int


def another_convert(value):
    """
    Convert to an integer. Safer. But note the use of pass. Absolutely not. We want to get rid of this.
    """
    the_int = -1
    try:
        the_int = int(value)
    except (ValueError, TypeError):
        pass
    return the_int


def yet_another_convert(value):
    """
    Convert to an integer. Better yet. Clarity and parsimony of code. But that -1 though...
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return -1


def informative_convert(value):
    """
    Convert to an integer.  Prints a very helpful error message! Probably best version.
    """
    try:
        return int(value)
    except (ValueError, TypeError) as e:
        print("Conversion error: {} returning None".format(str(e)), file=sys.stderr)
        return None
