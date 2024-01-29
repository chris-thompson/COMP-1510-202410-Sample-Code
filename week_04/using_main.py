"""
In programming, we try to avoid putting lines of code at random in a
module (aka a source file).

When we import a file to be used in our program, every single line gets
executed by the Python runtime. Yes, it even executes the function
definitions. We execute the definitions by binding the name of the function
to the code inside, and then we assign that function an address.

By placing everything inside function definitions, we avoid the case
where we might accidentally execute some code and/or generate output that
is not needed or desired.

We place all the code that "starts" the program inside the main function.

Most programming languages use a main function. It drives the program. We
also say it is the "point of insertion into the program".

At the very bottom of our file is a special if-statement. This if-statement
tells the Python runtime that iff (if and only if) the module is executed as
a program, and not important, execute the code in main.
"""


def dunderize(name):
    return "__" + name + "__"


def main():
    print(dunderize("Jacky"))


if __name__ == "__main__":
    main()
