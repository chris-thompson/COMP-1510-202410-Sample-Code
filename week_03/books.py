"""
We use ALL_CAPS when naming constants.

A constant is a value that must never change.

The ALL_CAPS is a signal to other developers -- don't modify this variable!
"""

COVER_PRICE = 24.95
DISCOUNT = 0.4
SHIPPING_FIRST = 3.00
SHIPPING_OTHER = 0.75

quantity = int(input('Enter number of copies: '))

wholesale_price = round(COVER_PRICE - (COVER_PRICE * DISCOUNT), 2)
shipping = round(SHIPPING_FIRST + ((quantity - 1) * SHIPPING_OTHER), 2)
total_cost = (quantity * wholesale_price) + shipping

print('Total cost for', quantity, 'copies is $', total_cost)
