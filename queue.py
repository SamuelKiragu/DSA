# Using Dynamic Arrays
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, element):
        self.items.append(element)
        return element # Return the added element

    def dequeue(self):
        item = self.items.pop(0)
        return item # Return the removed element

# Using Singly Linked Lists
class Queue1:
    def __init__(self):
        pass

    def enqueue(self, element):
        pass

    def dequeue(self):
        pass

# Using Doubly Linked Lists
class Queue2:
    def __init__(self):
        pass

    def enqueue(self, element):
        pass
    
    def dequeue(self):
        pass
