"""
Can we swap two values by passing them to a separate swap function?

In Python this will not work. Python passes things by value. That is,
every variable stores a reference aka an address in memory. When we
pass a variable to a function, we are making a copy of the address
stored in the variable and we pass this value.

We are effectively creating an alias, another variable that points to the
same spot.

If we change the new variable and make it point to something else, absolutely
nothing changes to the first variable. Swap doesn't work.
"""


def swap(a, b):
    temp = a
    a = b
    b = temp


def main():
    first = 1
    last = 100
    print(first, last)
    swap(first, last)
    print(first, last)


if __name__ == "__main__":
    main()
