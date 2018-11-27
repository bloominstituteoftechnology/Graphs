"""
Simple graph implementation
"""
# {
#     '0': {'1', '3'},
#     '1': {'0'},
#     '2': set(),
#     '3': {'0'}
# }
# class Vertex:
#     def __init__(self, label, component=-1):
#         self.label = str(label)
#         self.component = component
#         # self.edge = set()
    
#     # def __str__(self):
#     #     print(self.label)

#     def __repr__(self):
#         return 'Vertex: ' + self.label

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        # self.components = 0

    def add_vertex(self, key):
        self.vertices[key] = []
        return self.vertices[key]

    def add_edge(self, key, t):
        if key not in self.vertices or t not in self.vertices:
            print('vertex not found')
        else:
            self.vertices[key].append(t)
            return self.vertices[key]

    # def add_vertex(self, vertex, edges=()):
    #     if vertex in self.vertices:
    #         raise Exception('Error: trying to add a vertex that is already there!!!')
    #     if not set(edges).issubset(self.vertices):
    #         raise Exception('Error: trying to add an edge to no vertices?!?!?!')
    #     self.vertices[vertex] = set(edges)

    # def add_edge(self, start, end, bidirectional=True):
    #     if start not in self.vertices or end not in self.vertices:
    #         raise Exception('Vertices to connect not in graph')
    #     self.vertices[start].add(end)
    #     if bidirectional:
    #         self.vertices[end].add(start)

# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(graph.vertices)