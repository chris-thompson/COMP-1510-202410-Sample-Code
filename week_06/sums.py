"""
When we pass a list to a function, remember we are actually passing the
reference to the list aka its address in memory.

Once we pass an address to a list, the function is allowed to
modify the contents of the list. The function cannot change the address
(reference) of the list, but the function can mutate the list by adding
elements or deleting elements or, if the elements in the list are mutable,
by mutating the elements in the list.

That's what we are doing here!
"""


def running_sum(values):
    """Modify values so that it contains the running sums of its original items.

    :param values: a possibly empty list of integers
    :precondition: values is a list that contains only integers
    :postcondition: the list will be modified to contain a running sum

    >>> some_list = []
    >>> running_sum(some_list)
    >>> some_list
    []

    >>> some_list = [42]
    >>> running_sum(some_list)
    >>> some_list
    [42]


    >>> some_list = [4, 0, 2, -5, 0]
    >>> running_sum(some_list)
    >>> some_list
    [4, 4, 6, 1, 1]
    """
    for element in range(1, len(values)):
        values[element] = values[element - 1] + values[element]


print(running_sum([]))
