"""
Input received using the input function is always a string.

We have to use the float function to "cast" the string (convert it)
to a float if we want to store it and use it as float.

We have to use the int function to "cast" the string (convert it) to
an integer if we want to store it and use it like an integer.
"""


# Get the desired future value.
future_value = float(input('Enter the desired future value: '))

# Get the annual interest rate.
rate = float(input('Enter the annual interest rate: '))

# Get the number of years that the money will appreciate.
years = int(input('Enter the number of years the money will grow: '))

# Calculate the amount needed to deposit.
present_value = future_value / (1.0 + rate) ** years

# Display the amount needed to deposit.
print('You will need to deposit this amount:', present_value)
