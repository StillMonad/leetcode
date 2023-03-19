import threading
import _thread
import functools
import sys


def time_limit(sec):
    """
    decorator that limits function execution time to given seconds when not in debug
    """

    def wrapper(f):
        @functools.wraps(f)
        def inner(*args, **kwargs):
            class TimeoutException(Exception):
                def __init__(self, msg=''):
                    self.msg = msg
            
            timer = threading.Timer(sec, lambda: _thread.interrupt_main())
            timer.start()

            # auto-cancel time limits on debug-mode
            # (stops on breakpoints are usually counted as valid timeouts):
            if hasattr(sys, 'gettrace') and sys.gettrace() is not None:
                timer.cancel()

            try:
                res = f(*args, **kwargs)
                return res
            except KeyboardInterrupt:
                raise TimeoutException(
                    f"*** Timed out ({sec} seconds) for operation for {f.__name__}. ***")
            finally:
                timer.cancel()

        return inner

    return wrapper
