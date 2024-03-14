"""
A simple person to help demonstrate filter, map, and reduce.
"""


class Person:
    """
    A simple Person has a name and an age.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Person(' + self.name + ', ' + str(self.age) + ')'
