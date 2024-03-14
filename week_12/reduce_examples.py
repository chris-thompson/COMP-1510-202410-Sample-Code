from Person import Person
from functools import reduce


def main():
    """
    Drive the program.
    """
    data = [1, 3, 5, 2, 7, 4, 10]
    result = reduce(lambda total, value: total + value, data)
    print(result)

    data = [Person('Daniel', 54), Person('David', 21), Person('Dylan', 19)]
    total_age = reduce(lambda running_total, person: running_total + person.age, data, 0)
    average_age = total_age // len(data)
    print('Average age:', average_age)


if __name__ == '__main__':
    main()
