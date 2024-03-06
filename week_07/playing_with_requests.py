"""
Playing with the requests module.

The requests module is not included when we install
Python. We have to install it separately. If you mouse
over the import statement, you'll notice requests is
underlined in curly red. PyCharm will ask you if you
want it to install the requests module. Say yes.

The requests module is for HTTP requests. Super fun and
much easy.
"""

import requests


def download_page(url: str) -> str:
    """
    Download the specified page and return it as a string.

    :param url: The URL to download in string format
    :postcondition: Print the length and the first 250 character of the web content
    :postcondition: Create a string representing the URL content
    :return: A string representing the URL contents
    """
    res = requests.get(url)
    print(len(res.text))
    print(res.text[:250])  # prints the first 250 characters
    contents = res.text
    return contents


def main():
    """
    Drive the program.
    """
    value = download_page('https://www.gutenberg.org/files/28054/28054-0.txt')
    print(value)


if __name__ == "__main__":
    main()
