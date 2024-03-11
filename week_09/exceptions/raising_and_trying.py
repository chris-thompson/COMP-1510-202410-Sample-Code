"""
We raise errors in functions when we want the caller (user) to deal with the problem.

The caller (user) of the function must use try-except to deal with it and prevent
the program from crashing.
"""


def capitalize_name(name):
    """
    Capitalize the name. Uses title case.

    If the name has length 0, raises a Value Error.

    :param name: the name to capitalize (a string)
    :precondition: name is a string
    :postcondition: capitalize the name (using title case)
    :return: the capitalized name as a string
    :raises ValueError: if the name has zero length
    """
    if len(name) == 0:
        raise ValueError('No empty names allowed!')
    else:
        return name.title()


def main():
    """
    Drive the program.
    """
    capitalized_name = capitalize_name("tim berners-lee")
    print(capitalized_name)

    try:
        another_capitalized_name = capitalize_name("")
    except ValueError as e:
        print(e)
    else:
        print(another_capitalized_name)

    print(capitalize_name(""))


if __name__ == "__main__":
    main()
