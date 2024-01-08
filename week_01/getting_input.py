"""
We can use the input function to acquire data through the keyboard.

The input function always creates a string from the user's input.

We must convert the input to the correct type before we use it. We often
do it in the same line, like this?
"""

name = input('What is your name?: ')
age = int(input('What is your age? (Enter an integer): '))
income = float(input('What is your income? (Enter a floating point number): '))

print('Here is the data you entered:')
print('Name:', name)
print('Age:', age)
print('Income:', income)
