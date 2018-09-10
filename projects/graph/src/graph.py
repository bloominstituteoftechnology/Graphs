"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.verts = {}

    def add_vertex(self, label):
        if self.verts.get(label) == None:
            self.verts[label] = []
        else:
            return 'vertex already exists'

    def add_edge(self, x, y):
        if self.verts.get(x) == None:
            return f'{x} is not a vertex on the graph'
        elif self.verts.get(y) == None:
            return f'{y} is not a vertex on the graph'
        else:
            self.verts[x].append(y)
            self.verts[y].append(x)

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.verts)
