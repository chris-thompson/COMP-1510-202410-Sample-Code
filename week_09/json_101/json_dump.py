"""
Demonstrate how to dump a Python dict as a JSON "object".

We do this when we want to store Python in a file.

"""

import json


def main():
    """
    Drive the program.
    """
    word_count = {'the': 42, 'and': 37}
    filename = 'statistics.json'
    with open(filename, 'w') as file_object:
        json.dump(word_count, file_object)


if __name__ == "__main__":
    main()
