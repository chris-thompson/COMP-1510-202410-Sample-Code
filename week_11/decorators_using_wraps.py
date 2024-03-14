"""
Check out the wraps function in the functools module. We can use the wraps function
when decorating. We do this if it is important that the original information about
the original function remain available. Explore this example. """

from functools import wraps


def logger(function_to_be_logged):
    """
    Decorator to log a function by printing its name before invocation and after completion.

    :param function_to_be_logged: the function to be logged
    :precondition: function_to_be_logged is a function that takes no arguments
    :postcondition: function_to_be_logged is decorated with this decorator
    :return: the decorated function
    """
    @wraps(function_to_be_logged)
    def inner():
        print('Invoking', function_to_be_logged.__name__)
        function_to_be_logged()
        print('Returning from', function_to_be_logged.__name__)

    return inner


@logger
def greet():
    """
    Print a message to standard output.

    :postcondition: print a DeMorgan message to standard output
    """
    print("The negation of a disjunction is the conjunction of the negations.")


def main():
    """
    Drive the program.
    """
    greet()
    print('Function name:', greet.__name__)  # This is key
    print('Docstring: ', greet.__doc__)  # This is key
    print('Module: ', greet.__module__)


if __name__ == '__main__':
    main()
