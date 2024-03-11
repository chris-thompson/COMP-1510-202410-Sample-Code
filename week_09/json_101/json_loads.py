"""
Demonstrate how to acquire information from a JSON object that
has been formatted as a string.

We use load(s) which is easy to remember because of the s for string.

We do this when we want to open a JSON object in string-format. We
often need to do this when receiving JSON information passed from
a server to a client on the web.
"""


import json


def main():
    """
    Drive the program.
    """
    string_of_json_data = '{"name": "Larry", "isCat": true, "miceCaught": 0, "felineIQ": null}'
    python_dictionary = json.loads(string_of_json_data)
    print(type(python_dictionary))
    print(python_dictionary)


if __name__ == "__main__":
    main()
