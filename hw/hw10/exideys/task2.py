class Human:
    """Represent a human with a name."""

    species = "Homosapiens"

    def __init__(self, name: str) -> None:
        """
        Initialize a Human object.

        Args:
            name: Name of the human.
        """
        self.name: str = name

    def hello_message(self) -> str:
        """
        Return a greeting message.

        Returns:
            A greeting message with the human's name.
        """
        return f"Hello {self.name}"

    @classmethod
    def species_info(cls) -> str:
        """
        Return information about the human species.

        Returns:
            A message containing the human species.
        """
        return f"Human is a species of {cls.species}"

    @staticmethod
    def static_message() -> str:
        """
        Return an arbitrary static message.

        Returns:
            An arbitrary static message.
        """
        return "It's a static message"