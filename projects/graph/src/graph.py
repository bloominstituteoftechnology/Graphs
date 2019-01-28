"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vertex_1, vertex_2):
        self.vertices[vertex_1].add(vertex_2)

    def bft(self, starting_node):
        # create a queue
        q = dequeue()
        visited = set()
        # Enqueue the starting node
        q.append(starting_node)
        # while the queue is not empty,
        while q:
            pass
            # Dequeue a node form the queue
            # Mark it as visited
            # Enqueue all of its children that have not been visited

    def dtf(self, starting_node):
        # Create stack
        s = dequeue()
        visited = set()
        # Push the starting node
        s.append(starting_node)
        # while the stack is not empty,
        while s:
            pass
            # Pop a node from the stack
            # Mark it as visited
            # Push all of its children that have not been visited
    
    def dtf_r(self, starting_node, visited=None):
        if visited is None:
            visited = set()
        # If the node has not been visited
            # Mark the node as visited
            # Call dtf_r on all children
    
    def bfs(self, starting_node, target_node):
        # Create a queue
        q = dequeue()
        # create a visited list
        visited = set()
        # mark the first node as visited
        # enqueue the starting node
        q.append(starting_node)
        # while queue is not empty
        while q:
            pass
            # dequeue a node from queue
            # mark it as visited
            # if node == target return True
            # enqueue all of it's children
            


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)