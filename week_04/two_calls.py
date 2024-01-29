"""
What gets printed?
"""


def f(x):
    x = 2 * x
    return x


some_value = 1
some_value = f(some_value + 1) + f(some_value + 2)
print(some_value)
