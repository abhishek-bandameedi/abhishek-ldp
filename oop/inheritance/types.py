class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Generic animal sound"

# single inheritance

class Dog(Animal):      
    def bark(self):
        return "Woof!"

dog_obj = Dog("Buddy")
print(dog_obj.bark())   

class Cat(Animal):
    def meow(self):
        return "Meow!"
    
cat_obj = Cat("Whiskers")
print(cat_obj.meow()) 

#multiple inheritance

class Pet(Dog, Cat):    
    def play(self):
        return "Let's play!"
    
pet_obj = Pet("Fido")
print(pet_obj.speak())
print(pet_obj.play())

# Multilevel Inheritance

class Puppy(Dog):   
    def play(self):
        return "Let's play!"

puppy_obj = Puppy("Sparky")
print(puppy_obj.play()) 

#Hierarchical Inheritance

class DomesticCat(Cat): 
    def purr(self):
        return "Purr, purr!"
domestic_cat_obj = DomesticCat("Fluffy")
print(domestic_cat_obj.purr())


# method overriding
# The super().speak() calls the speak method from the parent class (Animal), and "Bark!" is added.

class Dog(Animal):      
    def speak(self):
        return super().speak() + " Bark!"   
    
dog1=Dog("Buddy")
print(dog1.speak())
