"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex in self.vertices:
            print("That vertex already exists")
            return False
        else:
            self.vertices[vertex] = set()        

    def add_edge(self, startpoint, endpoint):
        if startpoint not in self.vertices or endpoint not in self.vertices:
            print("Invalid start or endpoint")
            return False
        else:
            self.vertices[startpoint].add(endpoint)
            self.vertices[endpoint].add(startpoint)






# vertices = {
#     0: {1,2,3},
#     1: {0},
#     2: {0,3},
#     3: {0,2}
# }

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')

graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
print(graph.vertices.values())