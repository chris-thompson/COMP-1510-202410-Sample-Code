"""
Profiling is what we call timing a piece of code.

We profile it to determine how long it takes to execute.

There is a very quick and easy way to do this. The time
module contains a time function. It returns the current
time, in seconds since the beginning of the Epoch. We
can use this knowledge and some simple math to determine
how long some code takes to execute.

Note: Python is not fast. It's not a fast language. When
we want fast software, we can use something else. Python
is easy to use and develop and grow and it RULES the
artificial intelligence big data machine learning world
(for now, anyway!)

Better choices:

time.perf_counter and time.perf_counter_ns which
are performance counters. The latter returns the total
number of nanoseconds!

"""

import time


def main():
    """
    Drive the program. Demonstrate simple timing.
    """
    start_time = time.time()
    print(start_time)
    product = 1
    for granola in range(1, 100000):
        product = product * granola

    end_time = time.time()
    print(end_time)

    print('Took %f seconds to calculate.' % (end_time - start_time))

    # Consider how long it takes to perform this command!
    print('The result is %s digits long.' % (len(str(product))))


if __name__ == '__main__':
    main()
