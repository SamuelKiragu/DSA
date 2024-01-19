class SinglyNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f'Singly Node(data={self.data})'

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def __repr__(self) -> str:
        return f'Doubly Node(data={self.data})'

# Implementation of a singly linear linked list
# Uses Sentinel node
class SinglyLinkedList:
    def __init__(self):
        self.head = Node(None)
    
    def push(self, new_node):
        node = self.head
        while(node.next != None):
            node = node.next
        self.insert_after(node, new_node)

    def insert_after(self, node, new_node):
        new_node.next = node.next
        node.next = new_node
        return new_node #TODO: Find a better return value

    def remove(self, node):
        obsolete_node = node.data
        node.data = node.next.data
        node.next = node.next.next
        return obsolete_node

# Implementation of a Circularly Singly Linked List
# Uses Sentinel node
class CircularlySinglyLinkedList:
    def __init__(self):
        self.__sentinel = SinglyNode(data=None)
        self.__sentinel.next = self.__sentinel

    def insert(self, new_node):
        node = self.__sentinel.next
        while node is not self.__sentinel:
            node = node.next
        self.insert_after(node, new_node) 

    def insert_after(self, node, new_node):
        new_node.next = node.next
        node.next = new_node

    def insert_before(self, node, new_val):
        new_node = SinglyNode(node.data, node.next)
        node.data = new_val
        node.next = new_node

    def remove(self, node):
        if node is self.__sentinel:
            raise Exception('Can never remove sentiel.')
        removed_data = node.data
        node.data = node.next.data
        node.next = node.next.next
        return removed_data

# Implementation of Doubly Circularly Linked List
# Uses Sentinel node
class DoublyLinkedList:
    def __init__(self):
        self.__sentinel = Node(data=None)
        self.__sentinel.next = self.__sentinel
        self.__sentinel.prev = self.__sentinel

    def pop(self):
        return self.remove_by_ref(self.__sentinel.next)

    def pop_left(self):
        return self.remove_by_ref(self.__sentinel.next)

    def append_nodeleft(self, node):
        self.add_node(self.__sentinel, node)

    def append_node(self, node):
        self.add_node(self.__sentinel.prev, node)

    def append_left(self, data):
        node = Node(data=data)
        self.append_nodeleft(node)

    def append(self, data):
        node = Node(data=data)
        self.append_node(node)

    def remove_by_ref(self, node) -> Node:
        if node is self.__sentinel:
            raise Exception('Can never remove sentinel.')
        node.prev.next = node.next
        node.next.next = node.prev
        node.prev = None
        node.next = None
        return node

    def add_node(self, curnode, new_node):
        new_node.next = curnode.next
        new_node.prev = curnode
        curnode.next.prev = new_node
        curnode.next = new_node

    def search(self, value):
        self.__sentinel.data = value
        node = self.__sentinel.next
        while node.data != value:
            node = node.next
        self.__sentinel.data = None
        if node is self.__sentinel:
            return None
        return node

    def __iter__(self):
        node = self.__sentinel.next
        while node is not self.__sentinel:
            yield node.data
            node = node.next

    def reviter(self):
        node = self.__sentinel.prev
        while node is not self.__sentinel:
            yield node.data
            node = node.prev
