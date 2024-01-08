"""
The sort of script we can write in Python.
"""

# Constants
PRICE_PER_POUND = 14.99
SHIPPING_COST_PER_POUND = 0.89
ONLINE_CHARGE = 1.50
TAX_RATE = 0.13

# Get input from user
number_of_pounds = int(input("Enter pounds of coffee: \n"))

# Calculate costs and charges
subtotal = round(number_of_pounds * PRICE_PER_POUND, 2)
shipping_charges = round((number_of_pounds * SHIPPING_COST_PER_POUND) + ONLINE_CHARGE, 2)
tax = round((subtotal + shipping_charges) * TAX_RATE, 2)
total = round(subtotal + shipping_charges + tax, 2)

# Format and print the results
print('-'*32)
print(number_of_pounds, 'lbs @', PRICE_PER_POUND, '/ lb\t\t$', subtotal)
print('Shipping:\t\t\t\t$', shipping_charges)
print('Tax:\t\t\t\t\t$', tax)
print('-'*32)
print('Total:\t\t\t\t\t$', total)
print('-'*32)
