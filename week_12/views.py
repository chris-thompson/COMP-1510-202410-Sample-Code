"""
Views are not lists!
"""


def main():
    """
    Drive the program. When we view items in a dictionary, we are using a view object.

    A view object is like a list, but it's a different type of object. It retains a
    connection (a view) to the dictionary and when the dictionary changes, so does the view!
    """
    meals = {'bfast': 'egg', 'lunch': 'poke', 'dinner': 'spinach'}
    keys = meals.keys()
    values = meals.values()
    entries = meals.items()
    print(entries)
    print(type(keys))
    print(type(values))
    print(type(entries))
    del meals['bfast']
    print(entries)


if __name__ == '__main__':
    main()
