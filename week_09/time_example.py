"""
Python is fabulous but Python has a reputation for being slow.

Improvements introduced in Python 3.12 have brought tremendous speed improvements.

You can learn more here: https://docs.python.org/3/whatsnew/3.12.html

If you ever need to measure how long something takes, here's a fun way to do it!

Mentally bookmark this, we will use it...
"""

import time

t1 = time.perf_counter()

# Code to time goes here

t2 = time.perf_counter()

print('The code took {:.2f}ms'.format((t2 - t1) * 1000.))
