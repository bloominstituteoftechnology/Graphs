"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        pass  # TODO

  # node and vertex are the same
    def bfs(self, starting_node):
        # create a queue
        q = Queue()
        visited = set()
        # enquue the starting node
        q.Enqueue(starting_node)
        # while the queue is not empty
            # dequeue a node from the queue
            # mark it as visited
            # enqueue all of its children that have not been visited

      # node and vertex are the same
    def dfs(self, starting_node):
        # create a stack
        q = Stack()
        visited = set()
        # push the starting node
        q.Push(starting_node)
        # while the stack is not empty
            # pop a node from the stack
            # mark it as visited
            # push all of its children that have not been visited

