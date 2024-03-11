"""
Function annotations can be ignored. Look at this example. We
have annotated the add function so that it 'only' accepts
ints. But we have successfully used it with floats and with
strings. Run this -- no runtime errors, no crashes. But we
do get some warnings that are very hard to ignore. Mouse
over the two floats and the two strings for more information.
"""


def add(a: int = 5, b: int = 4) -> int:
    """
    Add two integers and return the sum.

    :param a: an integer
    :param b: an integer
    :precondition: a and b are integers
    :postcondition: calculate the sum of a and b
    :return: the sum as an integer
    """
    return a + b


def main():
    result = add(1, 2)
    print(result)
    result = add(1.0, 2.0)  # Does this work?
    print(result)
    result = add("Hello", "World")  # Does this work?
    print(result)
    result = add(5)  # What about this?
    print(result)


if __name__ == "__main__":
    main()
