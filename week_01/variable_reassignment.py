"""
In Python, we can assign a value to a variable. The variable stores the
address of that value, which is stored as zeros and ones
somewhere in memory.

We can assign a new value to a variable.

The new address of the new value created in memory overwrites
the existing address stored in the variable.

We do this a lot in programming.

Some programmers say that the variable points to a new value.
"""


dollars = 2.75
print('I have', dollars, 'in my account.')

# Reassign dollars so it references a different value.
dollars = 99.95
print('But now I have', dollars, 'in my account!')
