import linkedlist as ll

# Override Singly Linked List
# Remove Dummy Node
# Add Tail

class SinglyLinkedList(ll.SinglyLinkedList):
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

# Using Dynamic Arrays
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, element):
        return self.items.append(element) # Return the inserted element

    def dequeue(self):
        return self.items.pop(0) # Return the removed element

# Using Singly Linked Lists
class Queue1:
    def __init__(self):
        self.items = SinglyLinkedList()

    def enqueue(self, element):
        return self.items.push(element)

    def dequeue(self):
        return self.items.remove(self.items.head)

# Using Doubly Linked Lists
class Queue2:
    def __init__(self):
        pass

    def enqueue(self, element):
        pass
    
    def dequeue(self):
        pass
