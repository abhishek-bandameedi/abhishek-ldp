import pickle

# Pickle is a module in Python that provides a way to serialize and deserialize Python objects.
# Pickle is commonly used for saving and loading complex data structures, such as dictionaries, lists, and custom objects.

# Serialization: Serialization is the process of converting a Python object into a byte stream

data = {'name': 'John', 'age': 30, 'city': 'New York'}

with open('pickle/data.pickle', 'wb') as file:
    pickle.dump(data, file)

# Deserialization: Deserialization is the process of reconstructing a Python object from a byte stream.

with open('pickle/data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
