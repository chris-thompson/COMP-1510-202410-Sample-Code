import re


def main():
    """
    Drive the program. Demonstrate how to use the 'dot plus'.
    """
    name_regex = re.compile(r"First Name: (.+) Last Name: (.+)")
    user_input = 'First Name: Seven Last Name: of Nine'

    match_object = name_regex.search(user_input)
    if match_object:
        print("You entered:", match_object.group())
    else:
        print("Wrong input")


if __name__ == "__main__":
    main()
