import time


def timer(function_to_be_timed):
    """
    Decorate a function to find the runtime of the decorated function.

    :param function_to_be_timed: a function
    :precondition: function_to_be_timed is a function
    :postcondition: create a timer wrapper for function_to_be_timed
    :return: a wrapper to calculate the runtime of the decorated function
    """
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = function_to_be_timed(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {function_to_be_timed.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
def waste_some_time(number_of_times):
    """
    Waste some time.

    :param number_of_times: some large positive integer
    :precondition: num_times is a positive integer
    :postcondition: waste some time
    """
    for _ in range(number_of_times):
        sum([value ** 2 for value in range(number_of_times)])  # 🥵


def main():
    """
    Drive the program. Demonstrate how to decorate a function with a developer-made decorator.
    """
    waste_some_time(1000)
    waste_some_time(10000)


if __name__ == "__main__":
    main()
