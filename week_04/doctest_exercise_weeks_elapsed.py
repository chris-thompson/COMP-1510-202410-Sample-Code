def weeks_elapsed(first_day, second_day):
    """
    Return the number of full weeks that have elapsed between the two days.

    :param first_day: a positive integer
    :param second_day: a positive integer
    :precondition: first_day and second_day are days in the same year.
    :return: number of full weeks as an integer

    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)

    >>> weeks_elapsed(40, 61)

    """
