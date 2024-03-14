"""
Generators are an uncommon but useful tool.
"""


def gen_numbers():
    """
    Generate a sequence of numbers from 1 to 3.

    :postcondition: generate the next number in the sequence
    """
    yield 1
    yield 2
    yield 3


def gen_numbers_print():
    """
    Generate a sequence of numbers from 1 to 3 and print a fun message each time.

    :postcondition: generate the next number in the sequence
    """
    print('Start')
    yield 1
    print('Continue')
    yield 2
    print('Final')
    yield 3
    print('End')


def evens_up_to(limit):
    """
    Generate a sequence of even numbers from 0 to the limit inclusive.

    :param limit: a positive integer
    :precondition: limit is a positive integer
    :postcondition: generate the next number in the sequence
    """
    value = 0
    while value <= limit:
        yield value
        value += 2


def main():
    """
    Drive the program.
    """
    for value in gen_numbers():
        print(value)
    a_number_generator = gen_numbers()
    print(next(a_number_generator))
    print(next(a_number_generator))
    print(next(a_number_generator))
    # print(next(a_number_generator))
    print(next(gen_numbers()))  # Start over

    for value in gen_numbers_print():
        print(value)

    for value in evens_up_to(6):
        print(value, end=', ')
    print()

    for value in evens_up_to(4):
        print('value:', value, end=', ')
    print()

    for value in evens_up_to(6):
        print('value:', value, end=', ')
    print()

    evens = evens_up_to(4)
    print(next(evens), end=', ')
    print(next(evens), end=', ')
    print(next(evens), end=', ')

    #print(next(evens))


if __name__ == '__main__':
    main()
