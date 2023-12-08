import json

# json parsing

# JSON-formatted string
student='{"name": "John", "age": 30, "city": "New York"}'

# Parsing JSON string into a Python object
data = json.loads(student)

# 'data' is now a Python dictionary
print(data)


# json encoding

# Python dictionary
data2 = {"name": "Alice", "age": 25, "city": "London"}

# Encoding Python object into a JSON-formatted string
student2 = json.dumps(data)

# 'json_string' is now a JSON-formatted string
print(student2)


# JSON arrays

arr='[1, 2, 3, 4, 5]'
# parsing json array into python list
list=json.loads(arr)

print(list)

# customizing json encoding with json.dumps() method

# Python dictionary
data = {"name": "Alice", "age": 25, "city": "London"}

# Customizing JSON encoding with indentation
json_string = json.dumps(data, indent=2)

# 'json_string' is now a formatted JSON string
print(json_string)