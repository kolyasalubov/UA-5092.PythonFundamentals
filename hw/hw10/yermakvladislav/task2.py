class Human():
    def __init__(self, name):
        self.name = name
        
        
    def welcome(self):
        return f"Hi, I am {self.name}"
    
    
    @classmethod
    def species(cls):
        return "Homosapiens"
    
    @staticmethod
    def message():
        return "Work on the task is complete!"
    

vlad = Human("Vlad")
print(vlad.welcome())
print(Human.species())
print(Human.message())
