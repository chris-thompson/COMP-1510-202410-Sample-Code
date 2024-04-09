"""
A demonstration of profiling and optimizing using memoization.
"""

import time


def timer(func):
    """Print the runtime of the decorated function"""
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.30f} secs")
        return value
    return wrapper_timer


def fibonacci_memoization(nth_term, memory_structure):
    try:
        return memory_structure[nth_term]
    except KeyError:
        if nth_term == 0:
            memory_structure[nth_term] = 0
            return memory_structure[nth_term]
        elif nth_term == 1:
            memory_structure[nth_term] = 1
            return memory_structure[nth_term]
        result = fibonacci_memoization(nth_term - 1, memory_structure) + fibonacci_memoization(nth_term - 2, memory_structure)
        memory_structure[nth_term] = result
        return memory_structure[nth_term]


def fibonacci_recursive(nth_term):
    if nth_term == 0:
        return 0
    elif nth_term == 1:
        return 1
    else:
        return fibonacci_recursive(nth_term - 1) + fibonacci_recursive(nth_term - 2)


@timer
def fibonacci_manager(nth_term, memory_structure):
    return fibonacci_memoization(nth_term, memory_structure)


@timer
def fibonacci_manager_recursive(nth_term):
    return fibonacci_recursive(nth_term)


def main():
    """
    Drive the program. Behold. Memoization!
    """
    upper_bound = 500  # As upper_bound increases, the time difference does too. Wow!
    print(fibonacci_manager_recursive(upper_bound))
    dynamic_memory = {}
    print(fibonacci_manager(upper_bound, dynamic_memory))


if __name__ == "__main__":
    main()
