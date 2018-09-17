"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices={}

    def add_vertex(self, vertex):
        if vertex in self.vertices:
            raise Exception('Error: this vertex already exists')
        self.vertices[vertex]= set()

    def add_edge(self, startpoint, endpoint):
        if startpoint not in self.vertices or endpoint not in self.vertices:
            raise Exception('Error: one or more vertices do not exist')
        else:
            self.vertices[startpoint].add(endpoint)
            self.vertices[endpoint].add(startpoint)


graph = Graph()  # Instantiate your graph
graph.add_vertex('0') 
graph.add_edge('5','20')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)