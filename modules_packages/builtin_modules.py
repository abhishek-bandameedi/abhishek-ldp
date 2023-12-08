import math
import json

# math examples

print(math.sqrt(25))

print(math.pi)

print(math.floor(1.4))
print(math.ceil(1.4))

# json examples

#converting fromm json to python

x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# converting from python to json

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)