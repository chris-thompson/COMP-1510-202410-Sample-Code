"""
Working with sets.
"""


def main():
    """
    Drive the program.
    """
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)  # Duplicates have been removed!
    print(len(basket))

    for item in basket:
        print(item)

    print('apple' in basket)

    basket.remove('apple')
    basket.discard('apricot')  # WOW!
    print(basket)

    basket.add('apricot')
    print(basket)

    basket = {'apple', 'orange', 'banana'}
    basket.update(['apricot', 'mango', 'grapefruit'])
    print(basket)

    basket.clear()
    print(basket)

    some_fruit = {'apple', 'orange', 'banana'}
    other_fruit = {'grapefruit', 'lime', 'banana'}
    print('Union:', some_fruit | other_fruit)
    print('Intersection:', some_fruit & other_fruit)
    print('Difference:', some_fruit - other_fruit)
    print('Symmetric Difference:', some_fruit ^ other_fruit)

    set_of_size_one = {(1, 2, 3)}
    print(set_of_size_one)


if __name__ == '__main__':
    main()
