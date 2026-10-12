"""Module demonstrating instance, class and static methods with a Human class."""

class Human:
    """Class that represents a human with name."""

    def __init__(self, name: str) -> None:
        """
        Initialize human.

        Args:
            name: Human name
        """
        self.name = name

    def greet(self) -> str:
        """Return a greeting with the human's name."""
        return f"Hi {self.name}! Nice to see you here =)"

    @classmethod
    def species(cls) -> str:
        """Return the human species."""
        return "You are Homosapiens."

    @staticmethod
    def arbitrary_message() -> str:
        """Return an arbitrary message."""
        return "An arbitrary message."


def main():
    """Ask for a name and show the human's info."""
    while True:
        name = input("Enter your name: ")
        if name:
            new_human = Human(name)
            print(new_human.greet())
            print(Human.species())
            print(Human.arbitrary_message())

            break
        else:
            return "Invalid input"
    

if __name__ == "__main__":
    main()