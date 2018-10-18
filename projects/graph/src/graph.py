"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices ={}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist!")
        # {
        #     '0': set(),
        #     '1': {'4', '5'},
        #     '2':set(),
        #     '3':{4},
        #     '4': {'1','3'},
        #     '5': {'1'}
        # }
#This represents a graph with five vertices and three total (bidirectional) edges. 
# The vertex '0' and 2' have no edges, while '1' is connected to both '4' and '5', and '3' is connected to '4'.

graph = Graph() #Instantiate graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_edge('1', '4')
graph.add_edge('1', '5')
graph.add_edge('3', '4')
print(graph.vertices)