from collections import deque

# deque is a double ended queue 

# Create a deque
my_deque = deque([1, 2, 3])

# Append and pop elements


my_deque.append(4)      # append() will add element at end of queue
my_deque.appendleft(0)  # appendleft() will add element at begining of queue
print(my_deque)  

# Pop from the right and left
print(my_deque.pop())      # pop() will remove element from right of queue
print(my_deque.popleft())   # popleft() will remove element from left of queue