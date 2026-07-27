class calculator():
    """My calculator implementation"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Implementation of dotproduct calculation between two lists."""
        res = sum(a * b for a, b in zip(V1, V2))
        print(f"Dot product is: {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """List sum of its elements."""
        res = [a + b for a, b in zip(V1, V2)]
        print("Add Vector is : [" + ", ".join(f"{x:.1f}" for x in res) + "]")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """List subtraction of its elements."""
        res = [a - b for a, b in zip(V1, V2)]
        print("Sous Vector is: [" + ", ".join(f"{x:.1f}" for x in res) + "]")
