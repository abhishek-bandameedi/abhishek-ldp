# Instance methods: They are associated with the instance of a class.

class MyClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print(f"The value is: {self.value}")

# Creating an instance of the class
obj = MyClass(42)

# Calling an instance method
obj.display_value()
