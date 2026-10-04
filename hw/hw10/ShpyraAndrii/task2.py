class Human:
    species = 'Homosapiens'

    def __init__(self, name):
        self.name = name

    @classmethod
    def show_species_info(cls):
        return f"Species is '{cls.species}'"

    @staticmethod
    def show_some_message():
        return 'Some message'

    def welcome(self):
        print(f"Welcome, {self.name}!")


if __name__ == "__main__":
    for person in (Human("John"), Human("Jane")):
        person.welcome()
    print(Human.show_species_info())
    print(Human.show_some_message())
