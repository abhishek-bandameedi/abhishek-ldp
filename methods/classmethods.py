# Class methods: They are associated with the class rather than instance of class.

class MyClass:
    class_variable = 0

    def __init__(self, value):
        self.value = value

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1
        print(f"Class variable incremented to {cls.class_variable}")

# Creating instances of the class
obj1 = MyClass(10)
obj2 = MyClass(20)

# Calling a class method
MyClass.increment_class_variable()