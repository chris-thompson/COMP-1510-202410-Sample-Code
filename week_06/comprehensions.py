"""
Experiment with comprehensions.
"""


def main():
    """
    Drive the program. Use a debugger to see what is happening!
    """

    # What does this code do?
    counts = []
    for value in range(26):
        counts.append(0)

    # What does this code do?
    letters = [chr(letter) for letter in range(65, 91)]

    # What does this code do?
    tally = dict(zip(letters, counts))
    print(tally)

    # Is this efficient?
    tally_2 = {letter: count for letter in letters for count in counts}
    print(tally_2)


if __name__ == "__main__":
    main()
