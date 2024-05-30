from queue import Queue

# FIFO - first in first out

# Create a queue
my_queue = Queue()

# Enqueue elements
my_queue.put(1)
my_queue.put(2)
my_queue.put(3)

# Dequeue elements
while not my_queue.empty():
    print(my_queue.get())


    