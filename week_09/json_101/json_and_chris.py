"""
Demonstrate how to:

1. Load information from a JSON data file
2. Write some data from the JSON data set to a plaintext file
3. Access information inside the JSON object using dictionary-style
   square-bracket notation.
"""

import json


def main():
    """
    Drive the program.
    """
    with open('json_and_chris.json', 'r') as data:
        data_object = json.load(data)
        print(type(data_object))
        with open('json_and_chris.txt', 'w') as output:
            output.write(data_object['name'] + "'s Interests:\n")
            for interest in data_object['interests']:
                output.write(interest + "\n")


if __name__ == "__main__":
    main()




