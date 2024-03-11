"""
Demonstrate how to load a Python dict from a JSON "object".
"""

import json


def main():
    """
    Drive the program.
    """
    filename = 'statistics.json'
    with open(filename) as file_object:
        word_count = json.load(file_object)
    print(word_count)


if __name__ == "__main__":
    main()
