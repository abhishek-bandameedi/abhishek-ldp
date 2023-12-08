# Static Method: They are not bound to particular instance or class itself.

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# Calling static methods
result_sum = MathOperations.add(5, 3)
result_product = MathOperations.multiply(4, 6)
