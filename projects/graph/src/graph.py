"""
Simple graph implementation compatible with BokehGraph class.
"""
class Edge:     
    def __init__(self, destination):
        self.destination = destination

    def __repr__(self):
        return self.destination



class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = set()

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, label):
        if not label in self.vertices:
            new_vertex = Vertex(label)
            self.vertices[label] = new_vertex.edges

    def add_edge(self, label, destination):
        # if label in self.vertices and des
        new_edge = Edge(destination)
        self.vertices[label].add(new_edge)
        



graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)