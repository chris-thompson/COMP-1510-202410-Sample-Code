"""
We can learn a lot about scope by making small changes to this code snippet
and observing what gets printed out!
"""

x = 5


def f():
    # global x
    # print("Within f: x =", x)
    x = 9
    print("Within f: x =", x)


def main():
    print("Before f: x =", x)  # What gets printed?
    f()
    print("After f: x =", x)  # What gets printed?


if __name__ == "__main__":
    main()
