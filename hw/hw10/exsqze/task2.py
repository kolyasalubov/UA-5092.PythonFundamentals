class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f"Hello, my name is {self.name}.")

    @classmethod
    def get_species(cls):
        return "Homosapiens"

    @staticmethod
    def message():
        return 'Hellllllooooo'

person = Human('Maxym')
person.welcome_message()

print(Human.get_species()) 
print(Human.message())