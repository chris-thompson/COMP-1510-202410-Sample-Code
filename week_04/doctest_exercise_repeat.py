def repeat(some_string, number):
    """
    Return some_string repeated number times.

    If n is zero or negative, return the empty string.

    :param some_string: a string, of course
    :param number: an integer, possibly zero, possibly negative
    :precondition: some_string is a string
    :precondition: number is an integer
    :postcondition: returns a correctly multipled string

    >>> repeat('yes', 4)
    'yesyesyesyes'
    >>> repeat('no', 0)
    ''
    >>> repeat('no', -2)
    ''
    >>> repeat('yesnomaybe', 3)
    'yesnomaybeyesnomaybeyesnomaybe'
    """
