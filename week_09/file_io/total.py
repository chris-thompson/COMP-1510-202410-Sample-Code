"""
This is something new.  TextIO! and typing!
"""

from typing import TextIO


def sum_number_pairs(input_file: TextIO, output_file: TextIO) -> None:
    """
    Note the type of the input parameters! Neat!
    """
    for number_pair in input_file:
        # we know what this does
        number_pair = number_pair.strip()

        # Tokenize the string into a list of its constituent words
        operands = number_pair.split()

        # Access list members and cast
        total = float(operands[0]) + float(operands[1])

        # Use that neat format method for strings
        new_line = '{0} {1}\n'.format(number_pair, total)

        # Writes the output
        output_file.write(new_line)


def main():
    """
    Drive the program.
    """
    # Open two files at once
    with open('number_pairs.txt', 'r') as input_file, \
            open('number_pair_sums.txt', 'w') as output_file:
        # Pass both to a different function
        sum_number_pairs(input_file, output_file)


if __name__ == '__main__':
    main()
