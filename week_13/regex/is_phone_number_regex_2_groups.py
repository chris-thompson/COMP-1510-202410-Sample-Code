import re


def main():
    """
    Drive the program. This is much better.
    """
    phone_number_regex = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
    user_input = input("Enter a 10-digit phone number with dashes: ")
    match_object = phone_number_regex.search(user_input)
    if match_object:
        print('The phone number you entered is:', match_object.group())
        print('The phone number you entered is:', match_object.group(0))
        print('The phone number you entered is:', match_object.groups())  # TRICKY -- THERE IS AN S!
        print('The area code you entered is:', match_object.group(1))
        print('The exchange you entered is:', match_object.group(2))
        print('The subscriber number you entered is:', match_object.group(3))
        # print('The subscriber number you entered is:', match_object.group(-1))
    else:
        print("That's not a phone number.")


if __name__ == "__main__":
    main()
