import heapq

# heapq module provides implementation of heap queue algorithm.
# Create a heap
my_heap = [3, 1, 4, 1, 5, 9, 2]

# Convert the list into a heap
heapq.heapify(my_heap)

# Push and pop elements
heapq.heappush(my_heap, 6)
min_value = heapq.heappop(my_heap)

print(min_value)