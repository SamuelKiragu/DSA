import queue as q
import linkedlist as ll

# Create queue
my_queue = q.Queue()
my_queue1 = q.Queue1()

# Create nodes
node1 = ll.Node(21)
node2 = ll.Node(223)
node3 = ll.Node(50)
node4 = ll.Node(1)

# Add nodes to my_queue
my_queue.enqueue(node1)
my_queue.enqueue(node2)
my_queue.enqueue(node3)
my_queue.enqueue(node4)


# Add noteds to my_queue1
my_queue1.enqueue(node3)
my_queue1.enqueue(node1)
my_queue1.enqueue(node4)

# Remove nodes from my_queue
print(my_queue.dequeue())
print(my_queue.dequeue())


# Remove nodes from my_queue
print(my_queue1.dequeue())
