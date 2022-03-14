from time import sleep, perf_counter


def print_hello(name):
    print('hello ', name)


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
    print('hello ', name)
    end = perf_counter()
    print(end-start)


if __name__ == '__main__':
    print_hello("John")