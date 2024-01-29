"""
Demonstrate how to use a random number generator.
"""

import random


def roll_die(rolls, sides):
    """
    Roll a die with the specified number of sides the specified number of times.

    :param rolls: an int
    :param sides: an int
    :precondition: rolls must be an int
    :precondition: sides must be an int
    :postcondition: rolls the die of the specified size the specified number of times
    :return: random sum of rolls
    """
    return random.randint(rolls, sides * rolls)
