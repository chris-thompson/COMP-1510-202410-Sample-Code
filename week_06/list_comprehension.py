"""
Some introductory list comprehensions.
"""


def main():
    """
    Drive the program.
    """
    some_integers = [1, 2, 3, 4, 5, 6]
    print('some_integers:', some_integers)

    some_incremented_integers = [item + 1 for item in some_integers]
    print('some_incremented_integers:', some_incremented_integers)

    some_incremented_even_integers = [item + 1 for item in some_integers if item % 2 == 0]
    print('some_incremented_even_integers:', some_incremented_even_integers)


if __name__ == '__main__':
    main()
