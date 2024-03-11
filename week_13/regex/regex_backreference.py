import re


def main():
    """
    Drive the program. Demonstrate how to use a back reference.
    """
    while True:
        four_of_a_kind = re.compile(r"(.)\1{3}")
        user_input = input("Enter your text: ")
        match_object = four_of_a_kind.search(user_input)
        if match_object:
            print('You entered four of a kind:', match_object.group())
        else:
            print("Not acceptable.")


if __name__ == "__main__":
    main()
