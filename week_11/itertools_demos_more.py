import itertools


def main():
    """
    Drive the program. Here are some more neat things we can do with itertools.
    """
    # Chain sequences during iteration.
    chained_iterators = itertools.chain([1, 2, 3], [2, 3, 4])
    print(chained_iterators)

    # Iterate over an element repeated a specific number of times.
    repeated_value = list(itertools.repeat('hello', 5))
    print(repeated_value)

    # Omit elements during iteration using dropwhile and a predicate (lambda works wonders here).
    values = [1, 3, 5, 7, 9, 3, 1]
    dropwhile_values = list(itertools.dropwhile(lambda x: x < 5, values))
    print(dropwhile_values)

    # # Iterate over a slice!
    sliced_iterator = list(itertools.islice(values, 3, 6))
    print(sliced_iterator)


if __name__ == '__main__':
    main()
