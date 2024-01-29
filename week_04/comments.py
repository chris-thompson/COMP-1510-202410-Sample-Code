"""Module to demonstrate how to comment a function."""


def add_ints(a, b):
    """
    Return the sum of the two arguments.

    The first line of a docstring must be a short sentence that begins with a verb that describes
    the function's main role.

    After the first line, leave a blank line, then continue with your documentation.

    If you write the function header first, and then open a triple double quote multi-line comment,
    PyCharm will insert a docstring template for you to populate.

    Each parameter passed to a function requires its own param tag.  The param tag should list the
    parameter name and, if helpful, the data type that the function expects.

    A precondition is a requirement the user of the function agrees to meet before using the
    function. If the precondition is not met, the function is not guaranteed to work.

    A postcondition is something that the function promises will be true when it is finished, as
    long as the preconditions are met.

    The return tag describes what is returned.  If nothing is returned, None is implicitly returned (and
    we do not need to write a comment for that).

    :param a: an int
    :param b: an int
    :precondition: a must be an int
    :precondition: b must be an int
    :postcondition: calculate the sum of a and b
    :return: the sum of the arguments
    """
    total = a + b
    return total


def main():
    """
    Drive the program.
    """
    print(add_ints(1, 2))

    another_value = 10
    print(another_value)


if __name__ == "__main__":
    main()
