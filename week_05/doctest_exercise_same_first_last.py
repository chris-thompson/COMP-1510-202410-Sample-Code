def same_first_last(a_list):
    """
    Return True if and only if first item of the list
    is the same as the last item of the list.

    :param a_list: a list of course!
    :precondition: length(a_list) >= 2
    :postcondition: determines if the first/last elements are the same
    :postcondition: a_list is not modified
    :return: True if the first/last elements are the same, else False

    >>> same_first_last([3, 4, 2, 8, 3])
    True
    >>> same_first_last(['apple', 'banana', 'pear'])
    False
    >>> same_first_last([4.0, 4.5])
    False
    """
