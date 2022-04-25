"""
## Problem 2: extra
Implement the "slow down" logic. Create a function that will print some text. Create a decorator that takes an argument
time_to_sleep, which will be the number of seconds to sleep before executing the function. Decorate the function with
the described decorator and test the code with an example. You are free to add any additional logic to the function or
the decorator.
"""

from time import sleep, perf_counter


def slow_down(time_to_sleep):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            sleep(time_to_sleep)
            func(*args, **kwargs)

        return inner_wrapper

    return wrapper


@slow_down(time_to_sleep=5)
def print_hello(name):
    start = perf_counter()
    print("hello ", name)
    end = perf_counter()
    print(end - start)


if __name__ == "__main__":
    print_hello("John")
