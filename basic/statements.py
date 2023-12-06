#  Conditional Statement (if-elif-else)

x = 10
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# Loop Statements (for and while):

# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 3:
    print(count)
    count += 1

# Break and Continue Statements:

"""
break exits the loop prematurely.
continue skips the rest of the code inside the loop for the current iteration.
"""

for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print("continue",i)