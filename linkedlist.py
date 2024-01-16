class Node:
    def __init__(self, data, ref):
        self.data = data
        self.next = ref

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


