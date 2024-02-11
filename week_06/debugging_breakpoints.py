"""
Practice running this with the debugger. Set some breakpoints.
"""


def count_primates():
    primates = {"bonobos": 3, "gorillas": 14, "chimps": 36}
    for key, value in primates.items():
        print(f"{key} --- {value}")


def print_greeting(name):
    print(f"Good question {name}")


def main():
    count_primates()
    print_greeting("Chris")


if __name__ == "__main__":
    main()
