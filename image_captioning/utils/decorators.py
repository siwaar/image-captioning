"""
Some useful decorators
"""
import os
import time
from datetime import timedelta
from functools import wraps
from typing import Any, Callable, TypeVar, cast

import psutil

F = TypeVar("F", bound=Callable[..., Any])


def timeit(colored: bool = False) -> Callable[[F], F]:
    """Decorator to measure the time taken
    for executing the function
    """

    def timeit_inner(func: F) -> F:
        @wraps(func)
        def timeit_wrapper(*args: str, **kwargs: int) -> Any:
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            total_time = str(timedelta(seconds=round(end_time - start_time)))
            msg = f"Function {func.__name__} Took {total_time}"
            if colored:
                msg = f"\x1b[6;30;42m {msg} \x1b[0m"
            print(msg)
            return result

        return cast(F, timeit_wrapper)

    return timeit_inner


def memoryit(include_pid: bool = False) -> Callable[[F], F]:
    """Decorator used to measure the
    footprint of the function before and
    after its execution
    """

    def memory_usage(pid: int = os.getpid()) -> str:
        """
        Return memory usage
        """
        usage = psutil.Process(pid).memory_info()
        global_memory = psutil.virtual_memory()
        return (
            f"Memory usage {psutil.Process(pid).memory_percent():.2f}%"
            f" RSS={usage.rss/(1024**2):.3f}MB"
            f" data={usage.data/(1024**2):.3f}MB\nGlobal memory:"
            f" \tFree:{global_memory.available/(1024**3):.1f}GB"
            f" \tUsed:{global_memory.used/(1024**3):.1f}GB, \tPercent:"
            f" {global_memory.percent}%"
        )

    def memory_usage_inner(func: F) -> F:
        @wraps(func)
        def memory_wrapper(*args: str, **kwargs: int) -> Any:
            pid_str = f"[pid = {os.getpid()}] " if include_pid else ""
            print(f"{pid_str}Func {func.__name__} {memory_usage()}")
            result = func(*args, **kwargs)
            print(f"{pid_str}Func {func.__name__} {memory_usage()}")
            return result

        return cast(F, memory_wrapper)

    return memory_usage_inner


def debug(func: F) -> F:
    """Prints function signature and return value"""

    @wraps(func)
    def wrapper_debug(*args: str, **kwargs: int) -> Any:
        # formatting args and kwargs
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)

        print(f"Now calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"Call with {func.__name__}({signature}) -> returned {result!r}")

        return result

    return cast(F, wrapper_debug)
