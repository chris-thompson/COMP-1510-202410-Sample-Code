import math


def distance(x0, y0, x1, y1):
    """
    Calculate the distance between (x0, y0) and (x1, y1).

    :param x0: a number representing a point's x-value
    :param y0: a number representing a point's y-value
    :param x1: a number representing a second point's x-value
    :param y1: a number representing a second point's y-value
    :precondition: x0 must be a number
    :precondition: y0 must be a number
    :precondition: x1 must be a number
    :precondition: y1 must be a number
    :postcondition: calculate the distance between the two points
    :return: the distance between (x0, y0) and (x1, y1) as a float
    """
    return math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
