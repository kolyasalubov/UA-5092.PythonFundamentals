class Human:
    """Клас, що описує людину"""
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        """Виводить привітання для конкретної людини"""
        print(f"Вітаємо, {self.name}!")

    @classmethod
    def get_species(cls):
        """Повертає інформацію про біологічний вид"""
        return 'Species: "Homosapiens"'

    @staticmethod
    def arbitrary_message():
        """Повертає довільне текстове повідомлення"""
        return "Це повідомлення є статичним текстом"

user_name = input("Введіть ім'я людини: ")
person = Human(user_name)

person.welcome_message()
print(Human.get_species())
print(Human.arbitrary_message())