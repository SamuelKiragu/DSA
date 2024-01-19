class Queue:
    def __init__(self):
        self.items = [] # Using a dynamic array

    def enqueue(self, element):
        self.items.append(element)
        return element # Return the added element

    def dequeue(self, element):
        item = self.items.pop(0)
        return item # Return the removed element

