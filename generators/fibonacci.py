# Generators can represent infinite sequences without requiring infinite memory.

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the generator
for fib in fibonacci_generator():
    if fib > 100:
        break
    print(fib)
