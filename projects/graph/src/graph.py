"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if not vertex in self.vertices:
            self.vertices[vertex] = set()
        else:
            print('This vertex is already part of the graph.  Please try again.')

    def add_edge(self, vert1, vert2):
        # if both vert1 and vert2 are valid vertices found in self.vertices...
        if self.vertices[vert1] != None and self.vertices[vert2] != None:
            # if an edge has not already been created from vert1 to vert2, add edge to self.vertices
            if (not vert2 in self.vertices[vert1]) and (not vert1 in self.vertices[vert2]):
                self.vertices[vert1].add(vert2)
                self.vertices[vert2].add(vert1)
            else:
                print('This edge had already been created.  Please try again.')
                
        else:
            print('Please provide a valid set of vertices in the graph.')

# test
graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)