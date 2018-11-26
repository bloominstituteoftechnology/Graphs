"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, vertex):
        if vertex not in self.vertices.keys():
            self.vertices[vertex]= {0}


    def add_edge(self, edge, vertex):
        if vertex in self.vertices.keys():
            if self.vertices[vertex] == {0}:
                self.vertices[vertex] = {edge}
                print(self.vertices[vertex])
            else:
                self.vertices[vertex].update(edge)
                 
        else:
            raise ValueError
    
    


graph = Graph()  # Instantiate your graph
print(graph)
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('2', '1')
graph.add_edge('1', '2')
graph.add_edge('3', '2')
graph.add_edge('4', '4')
print(graph.vertices)