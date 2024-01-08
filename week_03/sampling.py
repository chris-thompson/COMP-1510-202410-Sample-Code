"""
Check out this amazing function available inside the random module!
"""
import random


def main():
    """
    Demonstrates how to use random.choices.

    We must provide two parameters:
        1. a population to choose from
        2. k, the number to choose.

    We MUST name the parameter, k = 3.  I'll show you why in a few weeks.  Trust me for now.

    It returns a list.  Go ahead and use the lovely join method available to strings.
    We start with an empty string and then to it we join all the individual strings in the list.

    Mic drop.  (Wait, can I still say that or is it already old news?)
    """
    population = "1234567890"
    selection = random.choices(population, k=3)   # You have to use k here, it is a named variable
    print(selection)
    final_answer = "".join(selection)
    print(final_answer)


if __name__ == "__main__":
    main()
