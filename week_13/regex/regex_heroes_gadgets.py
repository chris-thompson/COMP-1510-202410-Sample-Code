import re


def main():
    """
    Drive the program. Demonstrate how to use a group and the or operator.
    """
    while True:
        heroes_regex = re.compile(r'Bat(mobile|copter|bat|submarine)')
        user_input = input("Enter your favourite bat gadget ")
        match_object = heroes_regex.search(user_input)
        if match_object:
            print('The gadget you entered is:', match_object.group())
        else:
            print("Not acceptable.")


if __name__ == "__main__":
    main()
