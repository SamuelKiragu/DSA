class SinglyNode:
    def __init__(self, data, ref=None):
        self.data = data
        self.next = ref

        print(f'Created Node with data value: {self.data}')

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.nxt = nxt
        self.prev = prev
    
    def __repr__(self) -> str:
        return f'Node(data={self.data})'

# Implementation of a singly linear linked list
class SinglyLinkedList:
    def __init__(self):
        self.first_node = SinglyNode(None,None)
    
    def insert_after(self, node, new_node):
        new_node.next = node.next
        node.next = new_node

        print(f'Added node {new_node} after node {node}')

    def remove_after(self, node):
        obsolete_node = node.next
        node.next = obsolete_node.next

        print(f'Removed node {node}')
        # TODO: Destroy obsolete node

def iterate(self, some_node):
    if some_node != None:
        node = some_node
    while True:
        node = node.next
        if node != some_node: break

# Implementation of a Circularly singly linked list
class CircularlySinglyLinkedList:
    def __init__(self):
        self.last_node = None

    def insert_after(self, node, new_node):
        if node == None:
            new_node.next = new_node
        else:
            new_node.next = node.next
            node.next = new_node

        if self.last_node == node:
            self.last_node = new_node

    def insert_before(self, node, new_val):
        if node == None:
            new_node = SinglyNode(new_val, None)
            new_node.next = new_node
        else:
            new_node = SinglyNode(node.data, node.next)
            node.data = new_val
            node.next = new_node

    def remove(self, node):
        if node != None and len(self) > 1:
            removed_data = node.data
            node.data = node.next.data
            node.next = node.next.next
            return removed_data

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
        curnode.next.prev = newnode
        curnode.next = newnode

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
