"""
An example of two inner functions!
"""


def parent():
    """
    Q: What happens if we change the sequence of the inner functions
       inside the parent( ) function?
    Q: What happens if we try to invoke either of the inner functions from
       outside the parent( ) function, like in the main function?

    """
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()


def main():
    """
    Drives the program.
    """
    parent()


if __name__ == "__min__":
    main()
