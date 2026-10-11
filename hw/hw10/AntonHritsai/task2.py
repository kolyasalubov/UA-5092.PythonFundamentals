class Human:
    """This is a class representing a human being."""
    def __init__(self, name: str) -> None:
        """Initializes a new instance of the Human class."""
        self.name: str = name

    def greet(self) -> None:
        """Prints a greeting message."""
        print(f"Hello, {self.name}!")

    @classmethod
    def get_species(cls) -> str:
        """Returns the species of the human being."""
        return f"{cls.__name__} is Homosapiens!"

    @staticmethod
    def info() -> str:
        """Static method that returns information about the class."""
        return "This is a class representing a human being."