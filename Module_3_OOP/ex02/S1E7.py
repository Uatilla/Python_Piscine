from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True,
                 family_name="Baratheon", eyes="brown", hairs="dark"):
        """Initializing the Baratheon member."""
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """Killing the Baratheon member."""
        self.is_alive = False

    def __repr__(self):
        """Show the object representation."""
        return (
            f"Vector: ({repr(self.family_name)}, "
            f"{repr(self.eyes)}, "
            f"{repr(self.hairs)})"
        )

    def __str__(self):
        """Show the string representation."""
        pass


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(
        self,
        first_name,
        is_alive=True,
        family_name="Lannister",
        eyes="blue",
        hairs="light"
    ):
        super().__init__(first_name, is_alive)
        """Initializing the Lannister member."""
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """Killing the Lannister member."""
        self.is_alive = False

    def __repr__(self):
        """Show the object representation."""
        return (
            f"Vector: ({repr(self.family_name)}, "
            f"{repr(self.eyes)}, "
            f"{repr(self.hairs)})"
        )

    def __str__(self):
        """Show the string representation."""
        pass

    @classmethod
    def create_lannister(cls, name, alive=True):
        """Create a new Lanninster member"""
        return cls(name, alive)


def main():
    """Initialize the program."""
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jai = Lannister.create_lannister("Jai", True)
    print(f"Nm: {Jai.first_name, type(Jai).__name__}, Alv: {Jai.is_alive}")


if __name__ == "__main__":
    main()
