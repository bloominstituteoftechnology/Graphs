
class Vertex:
    def __init__(self, vertex):
        self.vertex = int(vertex)
        self.edges = set() 
    def __repr__(self):
        return f'{self.vertex}'

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        self.vertices[vertex] = Vertex(vertex)
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("This vertex does not exist!")

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
# graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('1', '2')
# graph.add_edge('0', '4')
print(len(graph.vertices))
print(graph.vertices)

