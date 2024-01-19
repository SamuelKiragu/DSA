import linkedlist as ll

_list = ll.DoublyLinkedList() # Create Doubly Circular Linked List

# Adding nodes to list
_list.append(10)
_list.append(23)
_list.append(43)
_list.append(54)

# Removing nodes from list
# TODO: Add logging to 
_list.pop()

# Searching value in list
# TODO: Implement various search algorithms here
value1 = 43
value2 = 23

print(_list.search(value1))
print(_list.search(value2))
