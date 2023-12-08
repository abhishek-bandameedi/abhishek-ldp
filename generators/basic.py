# Generator is a function that returns an iterator using the Yield keyword.
# Generators allow you to iterate over a potentially large sequence of data without the need to store the entire sequence in memory.
# yield statement allows the function to produce a series of values over time.
# Generators maintain their state between calls, allowing them to resume execution where they left off.

def square_generator(limit):
    n = 0
    while n < limit:
        yield n ** 2
        n += 1

# Using the generator
for square in square_generator(5):
    print(square)


# Generator expressions: 
# Similar to list comprehensions but use parantheses instead of square brackets

square_generator2 = (n ** 2 for n in range(5))

# Using the generator expression
for square in square_generator2:
    print(square)

# next() function is used to obtain next value from generator.

square_gen = square_generator(3)

print(next(square_gen))  
print(next(square_gen))  
print(next(square_gen))  

print()


# send() method is used to send a value back to genrator, which can be received using the yield statement.

def echo_generator():
    while True:
        received = yield
        print("Received:", received)

gen = echo_generator()
next(gen)            # Start the generator
gen.send("Hello")    # Send a value to the generator


# 'yield from' statement is used to delegate part of the operation to another generator.

def nested_generator():
    yield 1
    yield 2
    yield 3

def combined_generator():
    yield from nested_generator()
    yield 4
    yield 5

# Using the combined generator
for value in combined_generator():
    print(value)
