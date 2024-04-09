"""
It is important to be comfortable working with strings in programming.
"""


def main():
    """
    Drive the program.
    """
    print("Able was I ere I saw Elba")
    print("Sweatpants are a sign of defeat. You gave up, and you bought some sweatpants.")

    string_1 = 'Good'
    string_2 = " day"
    string_3 = string_1 + string_2
    print(string_3)
    print(len(string_3))

    my_variable = 'Jordan'
    print(my_variable)
    my_variable = "Eloise"
    print(my_variable)

    multi_line_string = """
    Hello
      World
    """
    print(multi_line_string)

    my_variable = 'Eunji'
    print(type(my_variable))

    greeting = 'hello world'
    print(greeting[4])
    print(greeting[1:5])
    print(greeting[:5])
    print(greeting[2:])

    print(greeting.upper())

    print(type(b'abc'))
    print(b'abc')

    title = 'The Good, The Bad, and the Resourceful'
    print('Source string:', title)
    print('Split using a space')
    print(title.split(' '))
    print('Split using a comma')
    print(title.split(','))

    my_string = 'Count, the number     of spaces'
    print("my_string.count(' '):", my_string.count(' '))

    welcome_message = 'Hello World!'
    print(welcome_message.replace("Hello", "Sayonara"))

    print('*' * 10)
    print('Hi' * 10)

    print('Bing Bing Bing and Bing'.find('Bing'))
    print('Bing Bing Bing and Bing'.find('Thompson'))

    print('James' == 'James')  # prints True
    print('James' == 'John')  # prints False
    print('James' != 'John')  # prints True
    print('James' == 'james')  # prints False

    some_string = 'Matcha latte with almond milk. Unsweetened.'
    print('Testing a String')
    print('-' * 20)
    print('some_string', some_string)
    print("some_string.startswith('H')", some_string.startswith('H'))
    print("some_string.startswith('h')", some_string.startswith('h'))
    print("some_string.endswith('d')", some_string.endswith('d'))
    print('some_string.istitle()', some_string.istitle())
    print('some_string.isupper()', some_string.isupper())
    print('some_string.islower()', some_string.islower())
    print('some_string.isalpha()', some_string.isalpha())

    print('String conversions')
    print('-' * 20)
    print('some_string.upper()', some_string.upper())
    print('some_string.lower()', some_string.lower())
    print('some_string.title()', some_string.title())
    print('some_string.swapcase()', some_string.swapcase())
    print('String leading, trailing spaces', "   xyz   ".strip())

    msg = 'This is the year ' + str(2014)
    print(msg)


if __name__ == '__main__':
    main()
