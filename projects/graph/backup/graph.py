"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vert_a, vert_b):
        if vert_a in self.vertices and vert_b in self.vertices:
            self.vertices[vert_a].add(vert_b)
        else:
            return 'exception occoured, one of the vertices is not in the Graph yet'

    def bft(self, starting_node):
        pass
        # create a queue
        # enqueue the starting node
        # while the queue is not empty:
            # Dequeue a node from the queue
            # mark it as visited
            # enqueue all of it's children that have not been visited

    def dft(self, starting_node):
        pass
        # Create a stack
        # push the starting node
        # while the stack is not empty:
            # pop a node from the stack
            # mark it as visited
            # push all of it's children that have not been visited

    def dft_r(self, starting_node, visited = None):
        if visited is None:
            visited = set()
        # if the node has not been visited:
            # mark the node as visited
            # call dft_r on all children
                # dft_r(child_node, visited)

# graph = Graph()
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(graph.vertices)
