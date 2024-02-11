"""
When a function is done, we want to return.

When we don't -- when we call another function without returning -- we
add a function call to the stack. The stack will fill up sooner than we
think. So we ensure we don't have a lot of loops between functions in
our code.

Profile your code. From the main menu, choose:

    Run > Run bad_program.py > Profile 'bad_program.py'

This program, when profiled, reveals no loops. We are not
stacking function calls on the call stack. Instead, when a function finishes
its work, it returns, and lets the calling function decide what to do next.

What is the largest number of function calls that will ever be on the
function call stack when we execute this code?

Compare this to bad_program.py
"""


def menu():
    while True:
        # does stuff
        do_something()


def do_something():
    user_input = input("Ask for data")  # Or calculate some value that can vary
    if user_input:  # Or if the value meets some test
        do_something_else()
    else:
        return None


def do_something_else():
    user_input = input("Ask for data")
    if user_input:
        return
    else:
        # do whatever has to be done
        return


def main():
    menu()


if __name__ == "__main__":
    main()

# Call stack

# do_something()
# menu
# main
