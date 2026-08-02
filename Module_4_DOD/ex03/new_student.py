import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random id of 15 characters"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Represent a student with automatic login and id generation"""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Compute login from name and surname, gen a random id"""
        self.login = self.name[0] + self.surname[0:]
        self.id = generate_id()


def main():
    """Main start of the program."""
    student = Student(name="Edward", surname="agle")
    print(student)
    # student2 = Student(name="Edward", surname="agle", id="toto")
    # print(student2)


if __name__ == "__main__":
    main()
