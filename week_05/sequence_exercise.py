"""
Consider a series where each number n is the sum of the 3 preceding numbers.
The series always starts with [0, 1, 1]. In this case the first 10 numbers of
the series are: [0, 1, 1, 2, 4, 7, 13, 24, 44, 81].

Write a program that generates these first 10 numbers and stores them in a
list. Your program must use a ‘for i in range’ loop. Your list should start
with 0, 1, 1 already in it.
"""


def generate_sequence(size):
    # replace this with your code
    return []


def main():
    seq = generate_sequence(int(input("How many do you want to generate?")))
    print("SEQ=", seq)


if __name__ == "__main__":
    main()
