"""
What does this do?
"""


def main():
    """
    Drive the program.
    """
    filename = 'pi_digits.txt'
    with open(filename) as file_object:
        lines = file_object.readlines()
        print(type(lines))

    for line in lines:
        print(line.rstrip())


if __name__ == '__main__':
    main()
