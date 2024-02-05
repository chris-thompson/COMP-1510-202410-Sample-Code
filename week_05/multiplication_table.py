"""
Cool things we can do with list and range functions.
"""


def print_table(size):
    """
    Print the multiplication table for numbers 1 through n inclusive.
    """
    numbers = list(range(1, size + 1))

    for number in numbers:
        print('\t' + str(number), end='')
    print()

    for number in numbers:
        print(number, end='')
        for other_number in numbers:
            print('\t' + str(number * other_number), end='')
        print()


def main():
    print_table(5)


if __name__ == "__main__":
    main()
