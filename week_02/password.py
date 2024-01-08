"""
We can compare strings using ==. We can also
compare ints and booleans using ==. Comparing
floating point numbers is a bit more complicated.
"""

password = input('Enter the password: ')

# Determine whether the correct password
# was entered.
if password == 'prospero':
    print('Password accepted.')
else:
    print('Sorry, that is the wrong password.')

