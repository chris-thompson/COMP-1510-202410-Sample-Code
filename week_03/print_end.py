"""
Check out the ways we can change how the print( ) function
ends each line.
"""


def convert_to_celsius(fahrenheit):
    """
    Return the number of Celsius degrees equivalent
    to Fahrenheit degrees.

    :param fahrenheit: a floating point number
    :precondition: fahrenheit is a float
    :postcondition: fahrenheit is converted to Celsius
    :return: the temperature concverted to Celsius as a float

    >>> convert_to_celsius(75)
    23.88888888888889
    """
    return (fahrenheit - 32.0) * 5.0 / 9.0


print('80, 78.8, and 10.4 degrees Fahrenheit are equal to ', end='')
print(convert_to_celsius(80), end=', \n')
print(convert_to_celsius(78.8), end=', and ')
print(convert_to_celsius(10.4), end=' Celsius.\n')
