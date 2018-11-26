"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, label):
        if label in self.vertices:
            raise "Vertex already exists.", label
        else:
            self.vertices[label] = set()
    
    def add_edge(self, label, destination):
        if label in self.vertices:
            if destination in self.vertices:
                self.vertices[label].add(destination)
            else:
                raise 'Destination does not exist.', destination
        else:
            raise 'Vertex does not exist.', label

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)