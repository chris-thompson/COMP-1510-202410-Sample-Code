"""
Demonstrate how to dump JSON into a string.

We use dump(s) which is easy to remember because of the s for string.

We do this when we want to create a JSON object in string-format. We
often need to do this when passing JSON information from server to client
on the web!
"""

import json


def main():
    """
    Drive the program.
    """
    word_count = {'the': 42, 'and': 37}
    string_version = json.dumps(word_count)
    print(type(string_version))
    print(string_version)


if __name__ == "__main__":
    main()
