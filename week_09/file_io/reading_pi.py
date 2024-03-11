"""
What will be printed here?
"""


def main():
    """
    Drive the program.
    """
    filename = 'pi_million_digits.txt'
    with open(filename) as file_object:
        lines = file_object.readlines()
        print(type(lines))
    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()  # What happens if we omit this? Explain why.
    print(type(pi_string))
    # print(pi_string)


if __name__ == "__main__":
    main()
