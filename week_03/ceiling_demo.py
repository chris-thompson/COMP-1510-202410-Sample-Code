"""
Demonstrates two methods for rounding a floating point number up
to the nearest integer.
"""
import math

user_input = float(input("Please enter a floating point number: "))
print("User input", user_input)

rounded_value = int(user_input)
print("Rounded value", rounded_value)

total_cans_of_paint = rounded_value + (user_input - rounded_value > 0)
print("Final total", total_cans_of_paint)

rounded_value_using_math = math.ceil(user_input)
print("Final total using math.ceil ", rounded_value_using_math)
