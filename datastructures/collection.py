from collections import namedtuple
from collections import defaultdict
from collections import Counter

# namedtuple
# Define a named tuple type
Person = namedtuple("Person", ["name", "age", "city"])

# Create an instance of the named tuple
person = Person(name="Alice", age=25, city="New York")

# Access fields 
print(person.name) 


# defaultdict
# Define a defaultdict with a default value of 0
word_counts = defaultdict(int)

# Increment the count for each word
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
for word in words:
    word_counts[word] += 1

print(word_counts)

# counter

# Count occurrences of elements in a list
elements = [1, 2, 3, 1, 2, 1, 4, 5, 3, 2, 1]
element_counts = Counter(elements)

print(element_counts)