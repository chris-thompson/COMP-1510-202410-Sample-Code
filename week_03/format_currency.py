"""
We can use the built-in format method to display a floating
point number as a currency.

What does the named parameter sep do? Try assigning different values
to it to find out.
"""


monthly_pay = 5000.0  # Is that enough to pay a mortgage in Vancouver?
annual_pay = monthly_pay * 12
print('Your annual pay is $', annual_pay)
print('Your annual pay is $', format(annual_pay, ',.2f'), sep='')
