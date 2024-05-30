import pickle

# You can pickle and unpickle custom objects by implementing the __reduce__ method in your class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __reduce__(self):
        return (self.__class__, (self.name, self.age))

person = Person('Alice', 25)

with open('pickle/person.pickle', 'wb') as file:
    pickle.dump(person, file)

with open('pickle/person.pickle', 'rb') as file:
    loaded_person = pickle.load(file)

print(loaded_person.name, loaded_person.age)
