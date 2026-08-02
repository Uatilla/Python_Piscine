def square(x: int | float) -> int | float:
    """Return the square of the given number."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return the number raised to the power of itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Return a closure that repeatedly applies the given function
    to the previous result, starting from x.
    """
    count = 0

    def inner() -> float:
        """
        Apply the stored function to the current
        value and return the new value."""
        count
        nonlocal x
        x = function(x)
        return x
    return inner


def main():
    """Main start of the program"""
    my_counter = outer(3, square)
    print(my_counter())
    # print(my_counter.__closure__)
    # print(my_counter.__closure__[1].cell_contents)
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()
