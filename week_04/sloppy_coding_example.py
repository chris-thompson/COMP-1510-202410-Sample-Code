"""
Don't write code like this. It is confusing. The
variable names don't tell me anything. The function
name is not helpful. The logic inside the function
should be simplified. The nested if statements can
be flattened to be easier to read through the
thoughtful use of Boolean operators.
"""


def f(a, b, c):
    if a:
        if b:
            print('hi')
        elif c:
            print('bonjour')
        else:
            print('hola')
    else:
        print('Select a language.')
