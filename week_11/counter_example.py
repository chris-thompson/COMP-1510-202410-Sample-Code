import collections


def main():
    """
    Drive the program. Demonstrate how to use Counter from the collections module.
    """
    fruit = collections.Counter(['apple', 'orange', 'pear', 'apple', 'orange', 'apple'])
    print(fruit)
    print(type(fruit))
    print(fruit['orange'])

    print('fruit.most_common(10):', fruit.most_common(10))

    some_fruit = collections.Counter(['apple', 'orange', 'pear', 'orange'])
    other_fruit = collections.Counter(['banana', 'apple', 'apple'])

    print('some_fruit:', some_fruit)
    print(type(fruit))
    print('other_fruit:', other_fruit)
    print(type(fruit))

    print('some_fruit + other_fruit:', some_fruit + other_fruit)
    print('some_fruit - other_fruit:', some_fruit - other_fruit)
    # Union (max(some_fruit[n], other_fruit[n])
    print('some_fruit | other_fruit:', some_fruit | other_fruit)
    # Intersection (min(some_fruit[n], other_fruit[n])
    print('some_fruit & other_fruit:', some_fruit & other_fruit)


if __name__ == '__main__':
    main()
