# enumerate is a built-in function in Python that is used to iterate over a sequence (such as a list, tuple, or string).
# It returns pairs containing the index and the corresponding item in the sequence.

# syntax:  enumerate(iterable,start=0)

students=['hanuman','ram','laxman']

for index,student in enumerate(students):
    print(f"index {index}: {student}")

# we can specify starting index 
for index,student in enumerate(students,start=1):
    print(f"index {index}: {student}")

# enumerating over strings

example="Hello"
for index,let in enumerate(example):
    print(f"index {index}: {let}")

# using zip()

fruits = ['apple', 'banana', 'cherry']
prices = [1.0, 0.5, 2.0]

for index, (fruit, price) in enumerate(zip(fruits, prices)):
    print(f"Index {index}: {fruit} - Price: {price}")

# creating dectionary 
fruits = ['apple', 'banana', 'cherry']
fruit_dict = {index: fruit for index, fruit in enumerate(fruits)}

print(fruit_dict)


