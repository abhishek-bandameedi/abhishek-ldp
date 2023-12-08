class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print(self.species,"Generic animal sound")

class Cat(Animal):
    def __init__(self, name):
        super().__init__("Cat")  # Animal.__init__(self,"Cat")
        self.name = name

    def speak(self):
        print(f"{self.name} says Meow!")

# Creating objects
animal = Animal("Unknown")
my_cat = Cat("Whiskers")

# Calling methods
animal.speak() 
my_cat.speak()         

