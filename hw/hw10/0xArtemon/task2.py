class Human:
    """
    A class representing a human with various method types.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a person with a name.
        """
        self.name: str = name

    def greeting(self) -> None:
        """
        Display a welcome message to the person (Instance Method).
        """
        print(f"Welcome, {self.name}")

    @classmethod
    def show_species(cls) -> str:
        """
        Return the species information (Class Method).
        """
        return "Homosapiens"

    @staticmethod
    def arbitrary_message() -> str:
        """
        Return an arbitrary message (Static Method).
        """
        return "This is an arbitrary static message."

if __name__ == "__main__":
    artem: Human = Human("Artem")
    artem.greeting()

    species_info: str = artem.show_species()
    print(species_info)
    species_info: str = Human.show_species()
    print(species_info)

    message: str = artem.arbitrary_message()
    print(message)
    message: str = Human.arbitrary_message()
    print(message)
