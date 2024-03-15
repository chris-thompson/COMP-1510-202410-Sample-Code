"""
How should we use the identity operator with None?
"""


def main():
    """
    Drive the program.
    """
    variable_that_stores_an_address = None
    print('variable_that_stores_an_address:', variable_that_stores_an_address)
    print('variable_that_stores_an_address is None:', variable_that_stores_an_address is None)
    print('variable_that_stores_an_address is not None:', variable_that_stores_an_address is not None)
    print(type(variable_that_stores_an_address))

    # Now set variable_that_stores_an_address to be True
    print('Set variable_that_stores_an_address to True')
    variable_that_stores_an_address = True
    print('variable_that_stores_an_address:', variable_that_stores_an_address)
    print('variable_that_stores_an_address is None:', variable_that_stores_an_address is None)
    print('variable_that_stores_an_address is not None:', variable_that_stores_an_address is not None)
    print(type(variable_that_stores_an_address))


if __name__ == '__main__':
    main()
