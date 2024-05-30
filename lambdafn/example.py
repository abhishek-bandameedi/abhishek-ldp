from functools import reduce

numbers = [1, 2, 3, 4, 5]

# lambda with map()

# Double each number using map and lambda
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)

# Lambda with filter()

# Filter even numbers using filter and lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# Lambda with reduce()


# Calculate the product of all numbers using reduce and lambda
product = reduce(lambda x, y: x * y, numbers)
print(product)
