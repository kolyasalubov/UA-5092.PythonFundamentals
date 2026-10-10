from __future__ import annotations

class Human:
    """
    A class representing a human being.
    """

    species_name: str = "Homosapiens"
    population: int = 0

    def __init__(self, name: str) -> None:
        """
        Initialize a new human with a name.
        """
        if not name or not name.strip():
            raise ValueError("Name cannot be empty.")
        self.name = name.strip()
        Human.population += 1

    def welcome(self) -> None:
        """
        Print a welcome message to the human.
        """
        print(f"Welcome, {self.name}!")

    @classmethod
    def species(cls) -> str:
        """
        Return the species information and current population count.
        """
        return f"{cls.species_name} (Current population: {cls.population})"

    @classmethod
    def get_population(cls) -> int:
        """
        Return the current population of humans.
        """
        return cls.population

    @staticmethod
    def message() -> str:
        """
        Return an arbitrary message.
        """
        return "Evolution made you stand upright — stop slouching at your desk! ;)"


if __name__ == '__main__':
    print(f"Initial species info: {Human.species()}")

    person1 = Human("Oleh")
    person1.welcome()

    person2 = Human("Anna")
    person2.welcome()

    print(f"Updated species info: {Human.species()}")
    print(f"Population count via classmethod: {Human.get_population()}")
    print(Human.message())
