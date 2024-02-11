"""
This is an example of how we can pass functions around as arguments to
other functions!

A function that has been defined in a source file will be given an
address in memory just like a variable or an object. We can use the
function's address to treat it like an object. We can store it in a
variable or we can pass it to another function.

We say that in Python functions are "first class." This is a computing
expression that many programmers use. It means we can pass functions
around to other functions. Not all programming languages do this!
"""


def operate(operation, first, second):
    return operation(first, second)


def add(first, second):
    return first + second


def append(first, second):
    return str(first) + str(second)


def prepend(first, second):
    return str(second) + str(first)


def main():
    first_value = int(input("Enter an integer: "))
    second_value = int(input("Enter an integer: "))
    alias_for_add_function = add
    print(operate(alias_for_add_function, first_value, second_value))
    print(operate(add, first_value, second_value))


if __name__ == "__main__":
    main()
