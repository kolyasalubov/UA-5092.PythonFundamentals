class Human:
    """Клас для представлення людини."""
    species: str = 'Homosapiens'

    def __init__(self, name: str) -> None:
        """Ініціалізує людину з її іменем."""
        self.name = name

    def welcome_message(self) -> str:
        """Повертає привітальне повідомлення для людини."""
        return f"Welcome, {self.name}! Nice to meet you."

    @classmethod
    def get_species(cls) -> str:
        """Повертає інформацію про вид, використовуючи атрибут класу."""
        return f"Species: {cls.species}"

    @staticmethod
    def arbitrary_message() -> str:
        """Повертає довільне статичне повідомлення."""
        return "This is an independent static message."


if __name__ == "__main__":
    person = Human("Naya")
    print(person.welcome_message())
    print(Human.get_species())
    print(Human.arbitrary_message())

