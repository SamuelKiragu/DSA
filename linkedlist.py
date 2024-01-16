class SinglyNode:
    def __init__(self, data, ref):
        self.data = data
        self.next = ref

class DoublyNode:
    def __init__(self, data, nxt, prev):
        self.data = data
        self.nxt = nxt
        self.prev = prev

# Implementation of a singly linked list
class SinglyLinkedList:
    def __init__(self, first_node):
        self.first_node = first_node
    
    def insert_after(self, node, new_node):
        new_node.next = node.next
        node.next = new_node

    def insert_beginning(self, lst, new_node):
        new_node.next = lst.first_node
        lst.first_node = new_node

    def remove_after(self, node):
        obsolete_node = node.next
        node.next = obsolete_node.next

    def remove_beginning(self, lst):
        obsolete_node = lst.first_node
        lst.fist_node = obsolete_node.next

    def iteration(self, some_node):
        if some_node != None:
            node = some_node
        while True
            # TODO:
            node = node.next
            if node != some_node: break

class CircularlySinglyLinkedList:
    # TODO:
