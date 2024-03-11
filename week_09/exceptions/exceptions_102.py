"""
Let's play with exceptions!
"""
import math


def function_can_throw(number):
    """
    Help demonstrate how to use exception handling.

    Raises a ValueError if number is not a positive integer.

    :param number: a positive integer
    :postcondition: calculate the factorial of number
    :return: the factorial of number as an integer
    :raises ValueError: if number is not a positive integer
    """
    if type(number) is not int or number < 0:
        raise ValueError("I can only process positive integers!")
    else:
        return math.factorial(number)


def main():
    """
    Drive the program.
    """
    try:
        product = function_can_throw("a")
    except ValueError as e:
        print(e)
    else:
        print(product)
    finally:
        print("This always happens!")


if __name__ == "__main__":
    main()
