class Human:
    """
    A human being with a name.
    """

    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls):
        return f"{cls.__name__} is a species of \"{cls.species}\""

    @staticmethod
    def random_message():
        return "Borshch is top dish!"


people = [Human("Anna"), Human("Bohdan"), Human("Olena")]
for person in people:
    person.welcome()

print(Human.get_species())
print(Human.random_message())
