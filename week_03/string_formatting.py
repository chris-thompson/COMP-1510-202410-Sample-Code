"""
Let's review some formatting options with strings.
"""


def main():
    """
    Drive the program.
    """
    format_string = 'Hello {}!'
    print(format_string.format('Phoebe'))

    name = "Keanu Reeves"
    age = 59
    print("{} is {} years old".format(name, age))

    format_string = "Hello {1} {0}, you got {2}%"
    print(format_string.format('Reynolds', 'Ryan', 47))

    format_string = "{artist} sang {song} in {year}"
    print(format_string.format(artist='Madonna', song='Material Girl', year=1984))

    print('|{:25}|'.format('25 characters width'))
    print('|{:<25}|'.format('left aligned'))  # Same as not specifying an alignment
    print('|{:>25}|'.format('right aligned'))
    print('|{:^25}|'.format('centered'))

    # Can format numbers with comma as thousands separator
    print('{:,}'.format(1234567890))
    print('{:,}'.format(1234567890.0))


if __name__ == '__main__':
    main()
