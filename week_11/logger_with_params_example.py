"""
We can use decorators for logging functions that accept parameters!
"""


def logger(function_to_be_logged):
    """
    Decorator to log a function by printing its name before invocation and after completion.

    :param function_to_be_logged: the function to be logged
    :precondition: function_to_be_logged is a function that takes two arguments
    :postcondition: function_to_be_logged is decorated with this decorator
    :return: the decorated function
    """
    def inner(first, second):
        print('Invoking', function_to_be_logged.__name__, 'with arguments:', first, 'and', second)
        function_to_be_logged(first, second)
        print('Returning from', function_to_be_logged.__name__)
    return inner


@logger
def my_func(something, something_else):
    """
    Print two values on one line.
    """
    print(something, something_else)


def main():
    """
    Drive the program.
    """
    my_func(4, 5)


if __name__ == '__main__':
    main()
