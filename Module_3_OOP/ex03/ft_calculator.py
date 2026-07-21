class calculator:
    """Build a basic operation calculator."""
    def __init__(self, vector):
        """Initialize the vector to be calculated."""
        self.vector = vector[:]

    def __add__(self, object) -> None:
        """Add the scalar object value to the vector."""
        self.vector = [round(x + object, 8) for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply the scalar object value with the vector."""
        self.vector = [round(x * object, 8) for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtract the scalar object value to the vector."""
        self.vector = [round(x - object, 8) for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide the scalar object value to the vector."""
        if object == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        else:
            self.vector = [round(x / object, 8) for x in self.vector]
            print(self.vector)


def main():
    """Init of the code."""
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5


if __name__ == "__main__":
    main()
