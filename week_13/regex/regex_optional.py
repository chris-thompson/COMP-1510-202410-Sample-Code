import re


def main():
    """
    Drive the program. Demonstrate how to use optional groups in a regular expression.
    """
    while True:
        # Example using the Bat®-clan
        batman_regex = re.compile(r'Bat(wo)?man')
        user_input = input("Who is your favourite superhero: ")

        match_object = batman_regex.search(user_input)
        if match_object:
            print("You selected:", match_object.group())
        else:
            print("Wrong answer")

        # Example using phone numbers
        phone_number_regex = re.compile(r"(\d\d\d-)?(\d\d\d)-(\d\d\d\d)")
        user_input = input("Enter your phone number, including the dashes:")
        match_object = phone_number_regex.search(user_input)
        if match_object:
            print("Your number is:", match_object.group())
        else:
            print("That's not a valid number")


if __name__ == "__main__":
    main()
