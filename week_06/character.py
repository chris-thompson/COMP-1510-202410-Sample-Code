"""
Check this out.

We have defined a global variable (gasp!). It's a dictionary that
represents the information we might store for a game character.

Note the functions in the module are concerned with one thing, and
only one thing: managing the character "object".

This is an example of a coherent module that could be used as part
of a larger program. If (and only if) we were allowed to use
global variables...
"""

character = {"name": None, "age": 0, "HP": 10, "X": 0, "Y": 0}


def get_age():
    return character['age']


def set_age(new_age):
    character['age'] = new_age


def get_name():
    return character["name"]


def set_name(new_name):
    character["name"] = new_name


def increment_hp():
    character["HP"] += 1


def take_damage(damage):
    character["HP"] -= damage
