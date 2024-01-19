import linkedlist as ll

_list = ll.CircularlySinglyLinkedList() # Create Singular Circular Linked List

# Creating new nodes for our list
node1 = ll.SinglyNode(234)
node2 = ll.SinglyNode(23)
node3 = ll.SinglyNode(32)
node4 = ll.SinglyNode(2)

# Add nodes to list
_list.insert(node1)
_list.insert(node2)
_list.insert(node3)
_list.insert(node4)

# Remove node from list
_list.remove(node4)

#TODO: Implement various search algorithms here

