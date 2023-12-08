# multiple except blocks

try:
    val=int(input("enter an integer: "))
    print(5/val)
except ValueError:
    print("Invalid input. Please enter an integer")
except ZeroDivisionError:
    print("can't divide by zero")


# Handling Multiple Exceptions in One Block

try:
    value = int(input("Enter an integer: "))
    result = 10 / value
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")