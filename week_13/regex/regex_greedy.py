import re


def main():
    """
    Drive the program. Demonstrate greedy algorithms.
    """
    while True:
        print("I am greedy. I take the minimum as soon as I can find it.")
        guffaw_regex = re.compile(r"(Ha){3,5}?")
        # print("I am not greedy. I search for the maximum and return it if I find it.")
        # guffaw_regex = re.compile(r"(Ha){3,5}")
        user_input = input("How funny is the joke?: ")

        match_object = guffaw_regex.search(user_input)
        if match_object:
            print("This funny:", match_object.group())
        else:
            print("Not funny.")


if __name__ == "__main__":
    main()
