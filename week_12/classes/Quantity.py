"""
Look at all the dunders.
"""


class Quantity:
    """
    A Quantity stores a value. The default value is 0.
    """
    def __init__(self, value=0):
        self.__value = value

    def __add__(self, other):
        new_value = self.__value + other.__value
        return Quantity(new_value)

    def __sub__(self, other):
        new_value = self.__value - other.__value
        return Quantity(new_value)

    def __mul__(self, other):
        new_value = self.__value * other.__value
        return Quantity(new_value)

    def __pow__(self, other):
        new_value = self.__value ** other.__value
        return Quantity(new_value)

    def __truediv__(self, other):
        new_value = self.__value / other.__value
        return Quantity(new_value)

    def __floordiv__(self, other):
        new_value = self.__value // other.__value
        return Quantity(new_value)

    def __mod__(self, other):
        new_value = self.__value % other.__value
        return Quantity(new_value)

    def __eq__(self, other):
        return self.__value == other.__value

    def __ne__(self, other):
        return self.__value != other.__value

    def __ge__(self, other):
        return self.__value >= other.__value

    def __gt__(self, other):
        return self.__value > other.__value

    def __lt__(self, other):
        return self.__value < other.__value

    def __le__(self, other):
        return self.__value <= other.__value

    def __str__(self):
        return 'Quantity[' + str(self.__value) + ']'


def main():
    """
    Drive the program. We are overriding operators. This is magical!
    """
    q1 = Quantity(5)
    q2 = Quantity(10)
    another_q = Quantity()
    print('q1 =', q1, ', q2 =', q2)
    q3 = q1 + q2
    print('q3 =', q3)
    print('q1 * q2 =', q1 * q2)
    print('q1 / q2 =', q1 / q2)
    print('q1 < q2: ', q1 < q2)
    print('q3 > q2: ', q3 > q2)
    print('q3 == q1: ', q3 == q1)


if __name__ == '__main__':
    main()
