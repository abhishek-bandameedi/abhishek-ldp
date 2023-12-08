try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("This will execute regardless of whether an exception occurred.")
