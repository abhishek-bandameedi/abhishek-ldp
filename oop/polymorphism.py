# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

class Vehicle:
  def __init__(self, brand):
    self.brand = brand

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

# function that works with any vehicle

def travel(vehicle):
  vehicle.move()


#Create a objects

car1 = Car("Ford") 
boat1 = Boat("Ibiza") 
plane1 = Plane("Boeing") 

# Polymorphic function calls

travel(car1)
travel(boat1)
travel(plane1)