import random


def simple_game():
    """
    Demonstrate acquiring input using a simple game.
    """
    lower = int(input("Enter your lower bound: "))
    upper = int(input("Enter your upper bound: "))
    secret_number = random.randint(lower, upper)
    guess = int(input(f"Enter a number between {lower} and {upper} inclusive: "))
    if guess == secret_number:
        print("You're right!")
    elif guess < secret_number:
        print(f"Too low, the number was {secret_number}")
    else:
        print(f"Too high, the number was {secret_number}")


def main():
    """
    Drive the program.
    """
    simple_game()


if __name__ == "__main__":
    main()
