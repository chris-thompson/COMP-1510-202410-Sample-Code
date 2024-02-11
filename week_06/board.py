"""
The pprint module lets us "pretty-print" things.

Check out how it prints the dictionary created from this
dictionary comprehension!
"""

import pprint


def make_board(width, height):
    """
    Create a board.
    :param width: The width of the board
    :param height: The height of the board
    :precondition: width is a positive non-zero integer
    :precondition: height is a positive non-zero integer
    :postcondition: creates a dict of tuple:string where the
                    key is coordinate tuple and the value is
                    the string description of the location
    :return: The board as a dictionary of tuple:string
    """
    return {(row, column): "This room is empty" for row in range(height) for column in range(width)}


def main():
    """
    Drive the program.
    """
    board = make_board(5, 5)
    print(board)
    print("And now the pretty print version:")
    pp = pprint.PrettyPrinter()
    pp.pprint(board)


if __name__ == "__main__":
    main()
