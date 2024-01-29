"""
We can use the code from some other module by importing the module.

This advises the Python compiler that there are functions, etc., that we will be using
that are defined in some other module (source file).
"""

import echo

print("__name__ is", __name__)
print(echo.__name__)

