"""
Hickory dickory dock
The mouse ran up the clock...
"""

import time


def main():
    """
    Hickory. Dickory. Dock. The mouse ran up the clock.
    """
    for _ in range(3):
        print('Tick')
        time.sleep(1)
        print('Tock')
        time.sleep(1)


if __name__ == '__main__':
    main()
