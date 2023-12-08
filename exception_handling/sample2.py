# try, else and finally
try:
    value = int(input("Enter an integer: "))
    result = 10 / value
except ValueError:
    print("Invalid input. Please enter an integer.")
else:
    print(f"Result: {result}")
finally:
    print("This block is always executed.")

# Raising exceptions

try:
    age = int(input("Enter your age: "))
    if age <= 0:
        raise ValueError("Age cannot be negative or zero.")
except ValueError as e:
    print(f"Error: {e}")
