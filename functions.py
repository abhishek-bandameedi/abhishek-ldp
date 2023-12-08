# Function definition
def greet(name):
    print(f"Hello, {name}!")

# Function invocation
greet("Alice")

def add(x, y):
    result = x + y
    return result

sum = add(3, 5)
print(sum) 

# default parameters

def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

greet_with_default()    
greet_with_default("Bob") 

# keyword arguments

def person(name,age):
    print(f"Name: {name}, Age: {age}")

person(age=22,name="Abhi")


# Arbitrary arguments

def print_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Specific Positional argument:", args[2])
    print("Keyword arguments:", kwargs)
    print("Specific Keyword argument:", kwargs["a"])

print_args(1, 2, 3, a="apple", b="banana")


#Passing list as an argument

def menu(items):
    for x in items:
        print(x)

fruits=["apple","banana","cherry"]
menu(fruits)

#lambda functions

multiply = lambda x, y: x * y
print("lambda function result: ",multiply(3, 4))


# Scope

def example():
    x=10  # local variable
    print(x)

example()
# print(x)  # this will result in error because x is not defined in this scope

# Global variable

gl_variable=20

def example2():
    # global gl_variable
    # gl_variable=30
    print("Inside the function:",gl_variable)

example2()
print("Outside the function:", gl_variable)