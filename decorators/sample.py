# Decorators allows programmers to modify the behaviour of a function or class.
# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.
# In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.


def my_decorator(func):
    def wrapper():
        print("Welcome to the website!")
        func()
        print("You have logged in successfully")
    return wrapper

@my_decorator
def login():
    print("Enter your credentials")
    print("credentials validated..")

login()

# decorators with parameters

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
