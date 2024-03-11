import re


def is_robot_name(the_name):
    """
    Return True if the name is a robot name, else False.

    A robot name can only contain letters and numbers.
    It must be no more than 10 characters long.
    The name must end with these four characters: 3000.

    :param the_name: a robot's name in string form
    :precondition: the_name is a string
    :postcondition: determines if the name is valid
    :return: True if the_name is valid, else False

    >>> is_robot_name('Andre3000')
    True

    >>> is_robot_name('3000Andre')
    False

    >>> is_robot_name('30003000')
    True

    >>> is_robot_name('Andre300000')
    False

    >>> is_robot_name('@13#$!~')
    False
    """

    if re.match(r'[A-Za-z0-9]{1,10}3000$', the_name):
        return True
    else:
        return False


def main():
    """
    Drive the program.
    """
    the_name = 'Andre3000'
    print(the_name, "is a robot name:", is_robot_name(the_name))


if __name__ == '__main__':
    main()
