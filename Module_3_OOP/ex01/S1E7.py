from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True,
                 family_name="Baratheon", eyes="brown", hairs="dark"):
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        self.is_alive = False

    def __repr__(self):
        return (
            f"Vector: ({repr(self.family_name)}, "
            f"{repr(self.eyes)}, "
            f"{repr(self.hairs)})"
        )

    def __str__(self):
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
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        self.is_alive = False

    def __repr__(self):
        return (
            f"Vector: ({repr(self.family_name)}, "
            f"{repr(self.eyes)}, "
            f"{repr(self.hairs)})"
        )

    def __str__(self):
        pass

    @classmethod
    def create_lannister(cls, name, alive=True):
        return cls(name, alive)
