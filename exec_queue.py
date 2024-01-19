import queue as q
import linkedlist as ll

# Create queue
my_queue = q.Queue()

# Create nodes
node1 = ll.Node(21)
node2 = ll.Node(223)
node3 = ll.Node(50)
node4 = ll.Node(1)

# Add nodes to queue
my_queue.enqueue(node1)
my_queue.enqueue(node2)
my_queue.enqueue(node3)
my_queue.enqueue(node4)

# Remove nodes from queue
print(my_queue.dequeue())
print(my_queue.dequeue())

