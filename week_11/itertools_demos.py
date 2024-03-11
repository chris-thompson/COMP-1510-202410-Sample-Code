"""
Demonstrate the use of some helpful functions in the itertools module.
"""

import itertools


def main():
    """
    Drive the program. These tools are very useful when iterating.
    """
    names = ["Arthur", "Eryn", "Inid", "Oliver", "Ursula", "Yorgan"]
    pairs = []
    for pair in zip(itertools.count(1), names):
        pairs.append(pair)
    print(pairs)

    evens = itertools.count(step=2)
    even_numbers = []
    for _ in range(10):
        even_numbers.append(next(evens))
    print(even_numbers)

    count_with_floats = itertools.count(start=0.5, step=0.75)
    float_sequence = []
    for _ in range(5):
        float_sequence.append(next(count_with_floats))
    print(float_sequence)

    choices = []
    boolean_generator = itertools.cycle([True, False])
    for _ in range(20):
        choices.append(next(boolean_generator))
    print(choices)

    permutations = list(itertools.permutations(['cyan', 'magenta', 'yellow']))
    print("There are %d permutations: " % len(permutations))
    for sequence_number, permutation in enumerate(permutations, 1):
        print("%d:\t%s" % (sequence_number, permutation))

    size = 2
    combinations = list(itertools.combinations(["ginger", "allspice", "cumin", "mint"], size))
    print("There are %d combinations of size %d: " % (len(combinations), size))
    for sequence_number, combination in enumerate(combinations, 1):
        print("%d:\t%s" % (sequence_number, combination))


if __name__ == "__main__":
    main()
