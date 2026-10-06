from __future__ import annotations

class Human:
    """
    A class representing a human being.
    """

    species_name: str = "Homosapiens"

    def __init__(self, name: str) -> None:
        """
        Initialize a new human with a name.
        """
        if not name or not name.strip():
            raise ValueError("Name cannot be empty.")
        self.name = name.strip()

    def welcome(self) -> None:
        """
        Print a welcome message to the human.
        """
        print(f"Welcome, {self.name}!")

    @classmethod
    def species(cls) -> str:
        """
        Return the species information of the class.
        """
        return cls.species_name

    @staticmethod
    def message() -> str:
        """
        Return an arbitrary message.
        """
        return "Evolution made you stand upright — stop slouching at your desk! ;)"


if __name__ == '__main__':
    person = Human("Oleh")
    person.welcome()

    print(Human.species())
    print(Human.message())
