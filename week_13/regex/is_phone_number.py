def is_phone_number(text: str) -> bool:
    """
    Validate the structure of a phone number in string format.

    This function is correct, I think. Is it? It's hard to tell.

    Yuck. It's so ugly.
    """
    if len(text) != 12:
        return False  # not phone number-sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False  # not an area code
    if text[3] != '-':
        return False  # does not have first hyphen
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False  # does not have first 3 digits
    if text[7] != '-':
        return False  # does not have the second hyphen
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  # does not have last 4 digits
    return True  # "text" is a phone number!


def main():
    """
    Drive the program.
    """
    print('415-555-4242 is a phone number:')
    print(is_phone_number('415-555-4242'))
    print('Moshi moshi is a phone number:')
    print(is_phone_number('Moshi moshi'))


if __name__ == "__main__":
    main()
