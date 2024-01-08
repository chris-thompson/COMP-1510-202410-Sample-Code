"""
Random numbers are ubiquitous in computing solutions.
"""
import random


def main():
    number = random.random()
    print(number)
    dice_roll = random.randint(20, 40)
    print(dice_roll)


if __name__ == "__main__":
    main()
