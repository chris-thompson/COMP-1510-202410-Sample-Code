"""
We can get module information using some special dunder variables.
"""

import random
import sys


def main():
    """
    Drive the program.
    """
    print(random.__name__)
    print(random.__doc__)
    print(random.__file__)
    print(dir(random))

    print('sys.version: ', sys.version)
    print('sys.maxsize: ', sys.maxsize)
    print('sys.path: ', sys.path)
    print('sys.platform: ', sys.platform)


if __name__ == '__main__':
    main()
