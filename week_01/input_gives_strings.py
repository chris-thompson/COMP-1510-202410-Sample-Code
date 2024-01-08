"""
We must remember that when we use the input function the operating system
will always cause our program to pause and wait for the user to enter a
value. That value is always passed to the Python runtime as a string.

If we want to treat input as something else, we must convert it.

In programming, we say we need to "cast" the value.

We do that by passing it to the int function or the float function, etc.

If we pass a suitable value, the characters will be extracted from the string
and converted to the type we want. If there are extra characters in there, for
example if we try to convert "Hello" to an integer, the program will crash
and produce a ValueError (all that red stuff that gets printed out).
"""


name = input('What is your name? ')
age = int(input('What is your age? '))
income = float(input('What is your income? '))

# Display the data.
print('Here is the data you entered:')
print('Name:', name)
print('Age:', age)
print('Income:', income)

