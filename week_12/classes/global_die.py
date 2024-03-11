import random

"""
We don't use global variables.

But. Imagine if we could. A file (module) could represent a single Die.

We could import the module and use it like it was an object.
 
It stores the state of the die as global variables.

It provides functions that let us use the die and modify the state.

This is a primitive object. With OOP, we move the object from the module to the heap!
"""
face_value = 1
number_of_sides = 1


def get_face_value():
    return face_value


def set_face_value(new_value):
    global face_value  # 🤮
    if 0 < new_value <= number_of_sides:
        face_value = new_value


def get_number_of_sides():
    return number_of_sides


def set_number_of_sides(new_size):
    global number_of_sides  # 🤮
    if new_size > 0:
        number_of_sides = new_size


def roll_die():
    global face_value  # 🤮
    face_value = random.randint(1, number_of_sides)
    return get_face_value()
