"""
We can use decorators for logging!
"""


def logger(function_to_be_logged):
    """
    Decorator to log a function by printing its name before invocation and after completion.

    :param function_to_be_logged: the function to be logged
    :precondition: function_to_be_logged is a function that takes no arguments
    :postcondition: function_to_be_logged is decorated with this decorator
    :return: the decorated function
    """
    def inner():
        print('Invoking ', function_to_be_logged.__name__)
        function_to_be_logged()
        print('Completed ', function_to_be_logged.__name__)

    return inner


@logger
def target():
    """
    Print a message to standard output.

    :postcondition: print a message to standard output
    """
    print('In target function')


def register(active=True):
    """
    Register a function for being logged.

    This is super cool. A wrapper that controls the behaviour of a wrapper!

    :param active: boolean True if function is to be invoked, else false
    :postcondition: if active is omitted, defaults to True
    :postcondition: decorate the function to be logged if active
    :return: the decorated function whose behaviour has been registered
    """
    def wrap(function_to_be_logged):
        def wrapper():
            print(function_to_be_logged.__name__, 'registration is', active)
            if active:
                function_to_be_logged()
                print('Invoked', function_to_be_logged.__name__)
            else:
                print('Did not invoke', function_to_be_logged.__name__)

        return wrapper

    return wrap


@register()
def simple_function():
    """
    Print something to standard output.
    """
    print('simple_function is printing')


@register(active=False)
def another_simple_function():
    """
    Print something to standard output.
    """
    print('another_simple_function is printing')


def main():
    """
    Drive the program.
    """
    target()
    # print('Function name:', target.__name__)  # What gets printed?
    # print('Docstring: ', target.__doc__)  # What gets printed?
    # print('Module: ', target.__module__)
    print('-' * 10)
    simple_function()
    print('-' * 10)
    another_simple_function()


if __name__ == '__main__':
    main()
