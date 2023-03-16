import time
import functools

def time_measure(f):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        st = time.time()
        res = f(*args, **kwargs)
        et = time.time()
        elapsed_time = et - st
        print(' == Execution time:', elapsed_time, 'seconds == ')
        return res
    return inner

@time_measure
def say_hi():
    print("hi")
