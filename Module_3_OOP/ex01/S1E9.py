from abc import ABC, abstractmethod


class Character(ABC):
    """Just being careful"""
    def __init__(self, name, is_alive=True):
        """Your docstring for Class"""
        self.first_name = name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Just being careful"""
        pass


class Stark(Character):
    """Your docstring for Constructor"""
    def die(self):
        """Your docstring for Method"""
        self.is_alive = False


def main():
    """Init of the code."""
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)


if __name__ == "__main__":
    main()
