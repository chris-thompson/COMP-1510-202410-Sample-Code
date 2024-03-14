def my_decorator(function_to_be_wrapped):
    """
    Decorate a function with simple print statements.

    :param function_to_be_wrapped: a function
    :precondition: function_to_be_wrapped is a function
    :postcondition: decorates the function with print statements
    :return: a decorated function
    """
    def wrapper():
        print("Something is happening before the function is called.")
        function_to_be_wrapped()
        print("Something is happening after the function is called.")
    return wrapper


def do_twice(function_to_be_called_twice):
    """
    Decorate a function with a wrapper that invokes it twice.

    :param function_to_be_called_twice: a function
    :precondition: function_to_be_called_twice is a function
    :postcondition: decorates the function with a wrapper that invokes it twice
    :return: a decorated function
    """
    def wrapper_do_twice(*args, **kwargs):
        function_to_be_called_twice(*args, **kwargs)
        function_to_be_called_twice(*args, **kwargs)
    return wrapper_do_twice


def decorate_and_return(function_to_be_decorated):
    """
    Decorate a function that returns a value.

    :param function_to_be_decorated: a function
    :precondition: function_to_be_decorated is a function
    :postcondition: decorates the function with a wrapper
    :return: a decorated function that returns a value
    """
    def wrapper_returns(*args, **kwargs):
        print("Something is happening before the function is called.")
        return function_to_be_decorated(*args, **kwargs)
    return wrapper_returns


@do_twice
def say_cake():
    """
    👁️️❤️🍰!
    """
    print("Cake! Gâteau! 케이크!, 蛋糕! bánh ngọt! Торт! केक!")


@my_decorator
def say_cake():
    """
    👁️️❤️🍰!
    """
    print("Cake! Gâteau! 케이크!, 蛋糕! bánh ngọt! Торт! केक!")


@decorate_and_return
def return_greeting(name):
    """
    Return a formatted greeting.

    :param name: a name
    :precondition: name is a string
    :postcondition: Create formatted greeting
    :return: a formatted greeting as a string
    """
    return f"Hi {name}"


@do_twice
def greet_with_cake(name):
    """
    Print a formatted greeting.

    :param name: a name
    :precondition: name is a string
    :postcondition: Print a formatted greeting
    """
    print(f"Cake for {name}!")


def main():
    """
    Drive the program.
    """
    say_cake()
    print('Function name:', say_cake.__name__)  # What gets printed?
    print('Docstring: ', say_cake.__doc__)  # What gets printed?
    print('Module: ', say_cake.__module__)
    greet_with_cake("everyone")
    hi_justin = return_greeting("Justin")
    print(hi_justin)


if __name__ == "__main__":
    main()
