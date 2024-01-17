class SinglyNode:
    def __init__(self, data, ref):
        self.data = data
        self.next = ref

class DoublyNode:
    def __init__(self, data, nxt, prev):
        self.data = data
        self.nxt = nxt
        self.prev = prev

# Implementation of a singly linear linked list
class SinglyLinkedList:
    def __init__(self):
        self.first_node = SinglyNode(None,None)
    
    def insert_after(self, node, new_node):
        new_node.next = node.next
        node.next = new_node

    def remove_after(self, node):
        obsolete_node = node.next
        node.next = obsolete_node.next
        # TODO: Destroy obsolete node

    def iteration(self, some_node):
        if some_node != None:
            node = some_node
        while True
            node = node.next
            if node != some_node: break

# Implementation of a Circularly singly linked list
class CircularlySinglyLinkedList:
    def __init__(self):
        self.first_node = SinglyNode(None, None)
        self.last_node = self.first_node

    def insert_after(self, node, new_node):
        pass

    def insert_beginning(self, lst, new_node):
        pass

    def remove_after(self, node, new_node):
        pass

    def remove_beginning(self, lst, new_node):
        pass

    def iteration(self, some_node):
        pass


