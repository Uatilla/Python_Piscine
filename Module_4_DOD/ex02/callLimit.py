from typing import Any


def callLimit(limit: int):
    """Decorator that limits the number of times a function can be called."""
    count = 0

    def callLimiter(function):
        """
        Receive the function and return a wrapper that enforces the call limit.
        """
        def limit_function(*args: Any, **kwds: Any):
            """
            Wrapper that counts calls and blocks execution after limit.
            """
            nonlocal count
            count += 1
            if count <= limit:
                function()
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter


@callLimit(3)
def f():
    """Prints f() function."""
    print("f()")


@callLimit(1)
def g():
    """Prints g() function."""
    print("g()")


def main():
    """Main start of the program."""
    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
