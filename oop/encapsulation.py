class Circle:
    def __init__(self, radius):
        self.__radius = radius  # Private attribute

    def get_radius(self):
        return self.__radius

    def area(self):
        return 3.14 * self.__radius ** 2

# Creating object
my_circle = Circle(5)

# Accessing private attribute using a getter method
print(f"Radius: {my_circle.get_radius()}")
print(f"Area: {my_circle.area()}")
