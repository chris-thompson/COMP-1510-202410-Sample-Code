"""
Remember functions are just objects with addresses!
"""


def get_msg():
    """
    Return a message.
    """
    return "Hello Python World!"


def main():
    """
    Drive the program.
    """
    message = get_msg()
    print(message)

    message = get_msg
    print(message)

    another_reference = get_msg
    print(another_reference())


if __name__ == '__main__':
    main()
