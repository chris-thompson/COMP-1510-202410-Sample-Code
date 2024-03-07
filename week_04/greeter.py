"""
This is another example of how we can treat functions as first class
objects in Python. In this case, I have assigned three string methods
to variables inside main. Then I can choose which of these methods
to apply to the string message input by the user.

Note that depending on which function we use, the other two are "greyed
out" in the source code. PyCharm is telling us that the two variables
are not being used in our code.

Generally, we like to remove unused code from our programs before we share
them. This reduces the "complexity" of our code. Our code becomes shorter
tidier easier to understand and grow!
"""


def greet(mode, message): # message.mode()
    greeting = mode(message)
    print(greeting)


def main():
    yell = str.upper
    whisper = str.lower
    confused_rasp = str.swapcase

    user_input = input("What is your announcement: ")
    greet(yell, user_input)


if __name__ == "__main__":
    main()
