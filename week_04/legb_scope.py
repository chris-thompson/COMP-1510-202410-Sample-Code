"""
When we talk about scope, we talk about LEGB:
 1. Local
 2. Enclosing
 3. Global
 4. then Built-in scopes.

What does this code do?
"""

global_variable = 'global_variable'


def outer(outer_parameter='outer_parameter'):
    local_variable_in_outer = 'local_variable_in_outer'
    global_variable = 'GLOBAL_VARIABLE'

    def inner():
        print(global_variable, outer_parameter, local_variable_in_outer)
    return inner()


def main():
    outer()
    print(global_variable)


if __name__ == "__main__":
    main()
