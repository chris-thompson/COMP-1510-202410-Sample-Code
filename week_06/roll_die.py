"""
Demonstrate how to use a random number generator.
"""

import random


def roll_die(rolls, sides):
    """
    Roll a die with the specified number of sides the specified number of times.

    :param rolls: a positive non-zero int
    :param sides: a positive non-zero int
    :precondition: rolls must be a positive non-zero int
    :precondition: sides must be aa positive non-zero int
    :postcondition: rolls the die of the specified size the specified number of times
    :return: random sum of rolls as an int
    """
    return random.randint(rolls, sides * rolls)
