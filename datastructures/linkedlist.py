class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        current = self.head
        if current and current.val == value:
            self.head = current.next
            return
        while current.next and current.next.val != value:
            current = current.next
        if current.next:
            current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

# Using the linked list
linked_list = LinkedList()
linked_list.insert(3)
linked_list.insert(2)
linked_list.insert(1)
linked_list.display()

linked_list.delete(2)
linked_list.display()
