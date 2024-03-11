import re


def main():
    """
    Drive the program. Demonstrate how to use the plus operator in regular expressions.
    """
    while True:
        # Example using the Bat®-clan
        batman_regex = re.compile(r'Bat(wo)+man')
        user_input = input("Who is your favourite superhero: ")

        match_object = batman_regex.search(user_input)
        if match_object:
            print("You selected:", match_object.group())
        else:
            print("Wrong answer")


if __name__ == "__main__":
    main()
