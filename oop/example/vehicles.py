class Vehicle:
    def __init__(self, brand, model):
        self._brand = brand  # Encapsulation: using underscore to indicate a protected attribute
        self._model = model

    def display_info(self):
        return f"{self._brand} {self._model}"

car = Vehicle("Toyota", "A")

# Accessing the information through a method (encapsulation)
print(car.display_info())


class Car(Vehicle):  # Car inherits from Vehicle
    def __init__(self, brand, model, color):
        super().__init__(brand, model)  # Inheriting attributes from the parent class
        self._color = color  

    def display_info(self):  # Overriding the method from the parent class
        return f"{self._color} {super().display_info()}"


my_car = Car("Ford", "Mustang", "Red")

print(my_car.display_info())


class Bike(Vehicle): 
    def __init__(self, brand, model, type):
        super().__init__(brand, model)
        self._type = type

# Function demonstrating polymorphism
def display_vehicle_info(vehicle):
    print(vehicle.display_info())


new_car = Car("Chevrolet", "Cruze", "Blue")
my_bike = Bike("Harley-Davidson", "Street 750", "Cruiser")

# Using the same function with objects of different classes
display_vehicle_info(new_car)
display_vehicle_info(my_bike)
