"""
Using the math module to calculate the distance between two points.
"""

import math


def main():
    # get input
    point1 = input('Enter first point, separate by a comma, i.e., 2, 8: ')
    point2 = input('Enter next point, separate by a comma, i.e., 2, 8: ')

    # Extract input and store in variables
    x1y1 = point1.split(',')
    x2y2 = point2.split(',')

    x1 = int(x1y1[0])
    y1 = int(x1y1[1])
    x2 = int(x2y2[0])
    y2 = int(x2y2[1])

    # Perform calculations
    lhs = (x2 - x1) ** 2
    rhs = (y2 - y1) ** 2
    distance = math.sqrt(lhs + rhs)

    # Print result
    print(round(distance, 1))


if __name__ == "__main__":
    main()
