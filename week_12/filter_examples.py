from Person import Person


def is_even(value):
    """
    Return True if value is even, False otherwise.

    :param value: an integer
    :precondition: value is an integer
    :postcondition: determines if value is even
    :return: True if value is even, else False
    """
    return value % 2 == 0


def main():
    """
    Drive the program.
    """
    data = [1, 3, 5, 2, 7, 4, 10]
    print('data:', data)

    # Filter for even numbers using a lambda function
    evens_using_lambda = list(filter(lambda value: value % 2 == 0, data))
    print('evens_using_lambda:', evens_using_lambda)

    # Filter for even numbers using a named function
    evens_using_function = list(filter(is_even, data))
    print('evens_using_function:', evens_using_function)

    data = [Person('Seogin', 16), Person('Shawn', 18), Person('Spring', 20)]
    for person in data:
        print(person, end=', ')

    print('\n-----')

    # Use a lambda to filter out children
    adults_only = list(filter(lambda candidate: candidate.age >= 18, data))
    for person in adults_only:
        print(person, end=', ')


if __name__ == '__main__':
    main()
