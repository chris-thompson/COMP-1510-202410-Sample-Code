"""
Demonstrate how to mock an object.

This function uses the input function.

How can we unit test this?
"""


def ask_for_value_and_convert_to_upper():
    return input("Enter your name please").strip().upper()
