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
        q = []
        visited = set()
        # enqueue the starting node
        q.append(starting_node)
        # while the queue is not empty:
        while len(q) > 0:
            # Dequeue a node from the queue
            n = q.pop()
            # mark it as visited
            visited.add(n)
            # enqueue all of it's children that have not been visited
            if self.vertices[n] != set():
                for item in self.vertices[n]:
                    if item not in visited:
                        q.append(item)

    def dft(self, starting_node):
        pass
        # Create a stack
        s = []
        visited = set()
        # push the starting node
        s.append(starting_node)
        # while the stack is not empty:
        while len(s) > 0:
            # pop a node from the stack
            n = s.pop(-1)
            # mark it as visited
            visited.add(n)
            # push all of it's children that have not been visited
            if self.vertices[n] != set():
                for item in self.vertices[n]:
                    if item not in visited:
                        s.append(item)

    def dft_r(self, starting_node, visited = None):
        if visited is None:
            visited = set()
        # if the node has not been visited:
        if starting_node not in visited:
            # mark the node as visited
            visited.add(starting_node)
            # call dft_r on all children
            if self.vertices[starting_node] != set():
                for item in self.vertices[starting_node]:
                    if item not in visited:
                        # dft_r(child_node, visited)
                        self.dft_r(item, visited)

# graph = Graph()
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(graph.vertices)
