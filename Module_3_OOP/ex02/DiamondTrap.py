from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Setting up a new king."""
    def __init__(self, first_name):
        """Initiliazing a new king."""
        super().__init__(first_name)

    def set_hairs(self, new_color):
        """Change the hair color."""
        self.hairs = new_color

    def set_eyes(self, new_color):
        """Change the eye color."""
        self.eyes = new_color

    def get_hairs(self):
        """Return the hair color."""
        return self.hairs

    def get_eyes(self):
        """Return the eye color."""
        return self.eyes


def main():
    """Initialize the code."""
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)
    print(King.__mro__)


if __name__ == "__main__":
    main()
