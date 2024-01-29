"""
Here's a helpful template for a menu-driven command line program.
"""


def get_user_command():
    command = input("Enter a command: ")
    return command


def some_function():
    """replace this with your function, and add more if you need to."""
    pass


def main():
    command = get_user_command()
    while command != "quit":
        if command == "[command name]":
            # Execute the correct function here
            some_function()
        command = get_user_command()


if __name__ == "__main__":
    main()
