class Human:
    """Represent a human with a name."""
    def __init__(self, name):
        self.name = name
    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls):
        return "Homosapiens"
    @staticmethod
    def message():
        return "Have a nice day!"

if __name__ == "__main__":
    person = Human("Andrii")
    person.welcome()
    print("Species:", Human.get_species())
    print(Human.message())