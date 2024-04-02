"""
Remember functions are just objects with addresses!
"""


def make_function():
    """
    Return a function that accepts two parameters and returns their sum.
    """
    def adder(first_argument, second_argument):
        return first_argument + second_argument

    return adder


def make_checker(instruction):
    """
    What does this function do?
    """
    if instruction == 'even':
        return lambda n: n % 2 == 0
    elif instruction == 'positive':
        return lambda n: n >= 0
    elif instruction == 'negative':
        return lambda n: n < 0
    else:
        raise ValueError('Unknown request')


def main():
    """
    Drive the program.
    """
    is_even = make_checker('even')
    is_positive = make_checker('positive')
    is_negative = make_checker('negative')
    print(is_even(3))
    print(is_positive(3))
    print(is_negative(3))

    what_do_i_do = make_function()
    print(what_do_i_do(3, 2))
    print(what_do_i_do(3, 3))
    print(what_do_i_do(3, 1))


if __name__ == '__main__':
    main()
