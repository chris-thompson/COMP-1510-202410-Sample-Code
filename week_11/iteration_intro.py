"""
What if we wat to use the iter and next functions directly?

Nothing says we can't. We may have some compelling reason to do this, though I cannot
think of any at this moment, I prefer to use abstraction.

But knowing how this works is good for a developer. We should know how a language is implemented
in order to take advantage of its quirks, strengths, and syntactic sugar.

What happens if we invoke print(next(myit)) a fourth time?
"""


def main():
    """
    Drive the program.
    """
    fruits = ("apple", "banana", "cherry")
    fruity_iterator = iter(fruits)
    print(next(fruity_iterator))
    print(next(fruity_iterator))
    print(next(fruity_iterator))

    # What happens if we uncomment the next line?
    # print(next(fruity_iterator))

    print(type(fruity_iterator))
    print(type(range(0, 1)))


if __name__ == "__main__":
    main()
