"""
A simple object to represent a point in 2D space.
"""

import math


class Point:
    """Represent a point in two-dimensional geometric coordinates."""

    def __init__(self, x=0, y=0):
        """Initialize the position of a new point. The x and y
           coordinates can be specified. If they are not, the
           point defaults to the origin (0,0)."""
        self.__y = y
        self.__x = x

    def move(self, x, y):
        """Move the point to a new location in 2D space."""
        self.__y = y
        self.__x = x

    def reset(self):
        """Reset the point back to the geometric origin: 0, 0"""
        self.move(0, 0)

    def calculate_distance(self, other_point):
        """Calculate the distance from this point to a second
        point passed as a parameter.

        This function uses the Pythagorean Theorem to calculate
        the distance between the two points. The distance is
        returned as a float."""

        return math.sqrt(
            (self.__x - other_point.__x) ** 2
            + (self.__y - other_point.__y) ** 2
        )


def main():
    """
    Drive the program.
    """
    # how to use it:
    point1 = Point()
    point2 = Point()
    point2.move(5, 0)
    point1.reset()
    print(point2.calculate_distance(point1))
    assert point2.calculate_distance(point1) == point1.calculate_distance(point2)
    point1.move(3, 4)
    print(point1.calculate_distance(point2))
    print(point1.calculate_distance(point1))


if __name__ == "__main__":
    main()
