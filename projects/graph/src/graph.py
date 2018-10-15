"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices={}
    def add_vertex(self,vertex):
        self.vertices[vertex]=set()
    def add_edge(self,vertex,edge):
        try:
            if self.vertices[vertex] is not None and self.vertices[edge] is not None:
                self.vertices[vertex].add(edge)
                self.vertices[edge].add(vertex)
        except:
            print('No such vertex exists.')
        

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
graph.add_edge('0', '4')
print(graph.vertices)