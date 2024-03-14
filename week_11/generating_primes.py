"""
A simple and practical use for a generator object.
"""


def prime_number_generator(bound):
    """
    Generate a sequence of prime numbers up to the bound inclusive.

    :param bound: a positive integer
    :precondition: 0 <= bound <= positive infinity
    :postcondition: create a generator object that yields prime numbers
    """
    # Assume that a number is a prime number until proved otherwise
    prime_number = True
    for candidate in range(2, bound):
        for potential_divisor in range(2, candidate):
            if candidate % potential_divisor == 0:
                prime_number = False
                break
        if prime_number:
            yield candidate  # What in the great Pythonic jungle is this?
        prime_number = True


def infinite_prime_number_generator():
    """
    Generate an infinite sequence of prime numbers.

    :postcondition: create a generator object that yields prime numbers
    """
    prime_number = True
    candidate = 2
    while True:
        for potential_divisor in range(2, candidate):
            if candidate % potential_divisor == 0:
                prime_number = False
                break
        if prime_number:
            yield candidate
        prime_number = True
        candidate += 1


def main():
    """
    Drive the program.
    """
    number = input('Please input the number:')

    if number.isnumeric():
        num = int(number)
        if num <= 2:
            print('Number must be greater than 2')
        else:
            for prime in prime_number_generator(num):
                print(prime, end=', ')
    else:
        print('Must be a positive integer')

    print('\n', '-' * 25)

    prime = infinite_prime_number_generator()
    print(next(prime))
    print(next(prime))
    print(next(prime))
    print(next(prime))
    print(next(prime))
    # while True:
    #     print(next(prime))


if __name__ == '__main__':
    main()
