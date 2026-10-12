class Human:
    """A class representing a human."""

    species = "Homosapiens"

    def __init__(self, name: str) -> None:
        self.name = name

    def welcome(self) -> None:
        print(f"Hello, {self.name}!")

    @classmethod
    def get_species(cls) -> str:
        return cls.species

    @staticmethod
    def write_text() -> str:
        return "Have a nice day!"


if __name__ == "__main__":
    person = Human("Anna")

    person.welcome()
    print(Human.get_species())
    print(Human.write_text())