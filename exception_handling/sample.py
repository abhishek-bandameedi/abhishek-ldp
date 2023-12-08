# sample example
try:
    print(x)
except:
    print("An exception occured")

# division by zero error

try:
    result=5/0 
except ZeroDivisionError as e:
    print(f"Error: {e}")


# generic except block

try:
    result=5/0 
except Exception as e:
    print(f"Error: {e}")