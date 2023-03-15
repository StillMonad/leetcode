import threading
import _thread
import functools


def limit_exec_time(sec):
    """
    decorator that limits function execution time to given seconds
    """

    def wrapper(f):
        @functools.wraps(f)
        def inner(*args, **kwargs):
            class TimeoutException(Exception):
                def __init__(self, msg=''):
                    self.msg = msg

            timer = threading.Timer(sec, lambda: _thread.interrupt_main())
            timer.start()
            try:
                res = f(*args, **kwargs)
                return res
            except KeyboardInterrupt:
                raise TimeoutException(
                    f"*** Timed out for operation for {f.__name__}. Should have taken less than {sec} seconds ***")
            finally:
                timer.cancel()

        return inner

    return wrapper
