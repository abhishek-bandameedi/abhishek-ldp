# we can apply multiple decorators to a single function or method.

def decorator1(func):
    def wrapper():
        print("Decorator 1: Something before the function is called.")
        result = func()
        print("Decorator 1: Something after the function is called.")
        return result
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2: Something before the function is called.")
        result = func()
        print("Decorator 2: Something after the function is called.")
        return result
    return wrapper

@decorator1
@decorator2
def my_function():
    print("Executing the main function.")

my_function()

# order of execution
# the above chain is similar to decorator1(decorator2(my_function))