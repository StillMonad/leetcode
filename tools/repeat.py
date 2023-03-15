import functools


def repeat(n):
    """
    decorator repeats function execution given times
    """

    def wrapper(f):
        @functools.wraps(f)
        def inner(*args, **kwargs):
            for _ in range(0, n):
                res = f(*args, **kwargs)
            return res

        return inner

    return wrapper
