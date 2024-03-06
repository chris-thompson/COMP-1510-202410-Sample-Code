"""
Command line arguments are provided in the command line.

When we invoke a program like this:
    python program_name

We can include command line arguments like this:
    python3 program_name -1 0 1 Hello 3.14 True Difficult 1-player
"""

import sys

print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))
