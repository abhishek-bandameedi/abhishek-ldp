
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 2)

# Accessing attributes
print(f"{dog1.name} is {dog1.age} years old.")
print(f"{dog2.name} is {dog2.age} years old.")

# Calling methods
dog1.bark()
dog2.bark()

#modify object properties

dog1.age=4
print(dog1.age)

# delete object properties

# del dog1.name
# dog1.bark()  # returns error because Dog object has no attribute 'name'

# delete objects

del dog1
dog1.bark() # returns error because dog1 is not defined