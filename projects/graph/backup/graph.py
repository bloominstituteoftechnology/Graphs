"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        pass  # TODO

    # def breadth_first_for_each(self, cb):
    #     queue = Queue()                     #Import Queue, Import Linked List
    #     queue.enqueue(self)
    #     # print('1', queue.size)
    #     while queue.size != 0:
    #     # print(queue.size)
    #     self = queue.dequeue()
    #     cb(self.value)
    #     if self.left:
    #         queue.enqueue(self.left)
    #     if self.right:
    #         queue.enqueue(self.right)
    
    # def bft(self, starting_node):
    #     # create a queue
    #     queue = Queue()

    #     Enqueue the starting_node
    #     # While the queue is not empty:
    #     while queue.size != 0:
    #         Dequeue a node from the queue
    #         Mark as visisted
    #         Enqueue all of its children (that have not been visisted)
# FIX!!!!
    #     # Mark the first node as visisted
    #     visited = set()             # or mark by color

# queue = []
# visited = {A, B, C, D, E, F, G}

# A
# B
# C 
# D
# E
# F 
# G 

# A is connected to all other nodes or reachable from all other nodes
# C can only reach E. C is reachable from B, F, and 


# Depth First
# ABDFCEG

    # def dft(self, starting_node):
    #     # create a stack
    #     s = Stack()
    #     visited = set()
    #     Push the starting_node
    #     # While the Stack is not empty:
    #         POP a node from the stack
    #         Mark as visited
    #         Push all of its children (that have not been visited)

    # DFT_recursive(self, starting_node, visited=None)
    # If the node has not been visisted (if visited is None, visited = set)
        # Mark the node as visited
        # Call DFT_recursive on all children