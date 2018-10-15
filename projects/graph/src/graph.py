class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

    def add_neighbor(self, vertex):
        if vertex not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            for key, value in self.vertices.items():
                if key == v1:
                    value.add_neighbor(v2)
                if key == v2:
                    value.add_neighbor(v1)
            return True
        else:
            return False
    
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))

# Test
# graph = Graph()
# graph.add_vertex(Vertex('0'))
# graph.add_vertex(Vertex('1'))
# graph.add_vertex(Vertex('2'))
# graph.add_vertex(Vertex('3'))
# graph.add_edge('0', '3') still not working
# graph.add_edge('0', '1') still not working
# print(graph.vertices)

