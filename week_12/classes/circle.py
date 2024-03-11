"""
A simple object to represent a circle with location and radius in 2D space.
"""

import math


class Circle:
    """Represent a circle with location and radius  in two-dimensional geometric coordinates."""

    def __init__(self, x: int, y: int, radius: int):
        """
        Create a Circle object.
        """
        self.__x = x
        self.__y = y
        if radius > 0:
            self.__radius = radius
        else:
            raise ValueError("You cannot create a circle with negative radius!")

    def get_x(self):
        """
        Get X Value.
        """
        return self.__x

    def get_y(self):
        """
        Get Y Value.
        """
        return self.__y

    def get_radius(self):
        """
        Get Radius.
        """
        return self.__radius

    def set_x(self, x_input: int):
        """
        Set X Coordinate.
        """
        self.__x = x_input

    def set_y(self, y_input: int):
        """
        Set Y Coordinate.
        """
        self.__y = y_input

    def set_radius(self, radius_input: int):
        """
        Set Radius.
        """
        if radius_input >= 0:
            self.__radius = radius_input
        else:
            raise ValueError("Radius cannot be negative")

    def get_circumference(self):
        """
        Get Circumference
        """
        return 2 * math.pi * self.__radius

    def get_area(self):
        """
        Get Area
        """
        return math.pi * (self.__radius ** 2)

    def __str__(self):
        """
        Return a string representation of this object
        """
        return 'X: ' + str(self.__x) + " Y: " + str(self.__y) + " Radius: " + str(self.__radius)


def main():
    """
    Drive the program.
    """
    try:
        Circle(0, 0, -1)
    except ValueError:
        print('Whoops, saved you from crashing!')

    try:
        Circle(0, 0, 1)
        print('It worked')
    except ValueError:
        print('You cannot create with a negative radius!')

    a_circle_instance = Circle(1, 3, 5)
    print(a_circle_instance.get_x())
    print(a_circle_instance.get_y())
    print(a_circle_instance.get_radius())

    a_circle_instance.set_x(7)
    a_circle_instance.set_y(11)
    a_circle_instance.set_radius(13)

    print(a_circle_instance.get_x())
    print(a_circle_instance.get_y())
    print(a_circle_instance.get_radius())

    print(a_circle_instance.get_circumference())
    print(a_circle_instance.get_area())

    print(a_circle_instance)


if __name__ == "__main__":
    main()

