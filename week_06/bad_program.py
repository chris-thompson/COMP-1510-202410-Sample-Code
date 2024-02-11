"""
When a function is done, we want to return.

When we don't -- when we call another function without returning -- we
add a function call to the stack. The stack will fill up sooner than we
think. So we ensure we don't have a lot of loops between functions in
our code.

Profile your code. From the main menu, choose:

    Run > Run bad_program.py > Profile 'bad_program.py'

This program, when profiled, reveals lots of loops. So we are never returning
to our calling point, instead, we are calling functions anew.

How big can the function call stack get before it overflows?

Compare this to good_program.py
"""


def menu():
    # does stuff
    do_something()


def do_something():
    user_input = input("Ask for data")  # Or calculate some value that can vary
    if user_input:  # Or if the value meets some test
        do_something_else()
    else:
        do_something()  # Try again


def do_something_else():
    user_input = input("Ask for data")
    if user_input:
        do_something_else()
    else:
        menu()


def main():
    menu()


if __name__ == "__main__":
    main()

# Represents the call stack
# menu
# do_something_else()
# do_something_else()
# do_something_else()
# do_something_else()
# do_something_else()
# do_something
# do_something
# do_something
# do_something
# do_something
# do_something
# do_something
# menu
# do_something_else()
# do_something_else()
# do_something_else()
# do_something_else()
# do_something_else()
# do_something
# do_something
# do_something
# do_something
# do_something
# do_something
# do_something
# menu
# main
