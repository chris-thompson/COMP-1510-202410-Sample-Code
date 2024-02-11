"""
Check this out. We call this slice assignment.

It's like assignment, but we replace a slice of addresses!
"""


def main():
    """
    Drive the program.
    """
    integers = list(range(0, 10))
    print(integers)
    integers[0] = 1
    print(integers)

    integers[4:6] = [-10]
    print(integers)

    integers[8:] = [-10, -10, -10, -10, -10]
    print(integers)

    integers[:] = [1, 2, 3]
    print(integers)


if __name__ == "__main__":
    main()
