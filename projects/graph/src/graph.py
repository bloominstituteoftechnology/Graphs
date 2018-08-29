

class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = set()

    def __repr__(self):
        return str(self.label)


class Graph:
    def __init__(self):
        # this is a dictionary of sets
        self.vertices = {}

    def insert_edge(self, start, end):
        if start not in self.vertices and end not in self.vertices:
            raise ValueError("No entries!")
        else:
            self.vertices[start].add(end)
            self.vertices[end].add(start)

    def insert_vertex(self, vertex):
        if vertex not in self.vertices:
            # turning the vertex into a set inside the dictionary
            self.vertices[vertex] = set()
        else:
            raise ValueError("Vertex already exists in set!")

    
# my_graph = Graph()
# node_one = Vertex('NodeOne')
# my_graph.insert_vertex(node_one)
# print(my_graph.vertices)
