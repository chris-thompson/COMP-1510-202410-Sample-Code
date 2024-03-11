import re


def main():
    """
    Drive the program. How does this work?
    """
    while True:
        user_input = input("Enter a 10-digit phone number with dashes: ")
        phone_number_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
        match_object = phone_number_regex.search(user_input)
        if match_object:
            print('The phone number you entered is: ', match_object.group())
        else:
            print("That's not a phone number.")


if __name__ == "__main__":
    main()
