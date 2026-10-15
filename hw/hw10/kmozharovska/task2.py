class Human:
    """Represent a human with a name."""
    def __init__(self, name: str) -> None:
        """Initialize a human with name."""
        self.name = name

    def greet(self) -> str:
        """Greet a human by name."""
        return f"Welcome, {self.name}!"

    @classmethod
    def return_species(cls) -> str:
        """Return the species of a human."""
        return "Your species is Homosapiens."

    @staticmethod
    def arbitrary_message() -> str:
        """Return an arbitrary message."""
        return "An arbitrary message."


def main() -> None:
    """Run the Human class demonstration."""
    while True:
        name = input("Enter your name: ")
        if name:
            break
        else:
            print("Invalid input.")
    person = Human(name)
    print(person.greet())
    print(Human.return_species())
    print(person.return_species())
    print(Human.arbitrary_message())
    print(person.arbitrary_message())


if __name__ == "__main__":
    main()
