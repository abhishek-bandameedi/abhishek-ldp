# sort with lambda

students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 28}
]

# Sort students by age
sorted_students = sorted(students, key=lambda student: student["age"])
print(sorted_students)


