from Person import Person


def increment(value):
    """
    Add value to 1 and return the result.

    :param value: a number
    :precondition: value is a number
    :postcondition: calculate the increment
    :return: value incremented by 1
    """
    return value + 1


def main():
    """
    Drive the program.
    """
    data = [1, 3, 5, 2, 7, 4, 10]
    print('data:', data)

    # Apply the lambda function to each element in the list using map
    incremented_using_lambda = list(map(lambda number: number + 1, data))
    print('incremented_using_lambda', incremented_using_lambda)

    # Apply the add_one function to each element in the using map
    incremented_using_function = list(map(increment, data))
    print('incremented_using_function:', incremented_using_function)

    odds = [1, 3, 5, 7]
    evens = [2, 4, 6, 8]

    result = list(map(lambda first, second: first + second, odds, evens))
    print(result)

    data = [Person('Nick', 19), Person('Nicky', 23), Person('Nolan', 29)]
    ages = list(map(lambda person: person.age, data))
    print(ages)


if __name__ == '__main__':
    main()
