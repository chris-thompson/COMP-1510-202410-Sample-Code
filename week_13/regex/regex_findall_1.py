import re


def main():
    """
    Drive the program. Demonstrate the difference between . and .* in the regular expression.
    """
    at_regex = re.compile(r".at")
    match_object = at_regex.findall('rThe fat cat and rat in the hat sat on the flat mat with pat to chat')
    print(match_object)

    at_regex = re.compile(r'.*at')
    match_object = at_regex.findall('The fat cat and rat in the hat sat on the flat mat with pat the bat to chat')
    print(match_object)


if __name__ == "__main__":
    main()
