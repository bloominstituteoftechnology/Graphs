"""
Simple graph implementation compatible with BokehGraph class.
"""

def counterCreator():
    counter = -1
    def increment():
        # nonlocal 
        nonlocal counter
        counter += 1
        return str(counter)
    return increment

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, node):
# if key doesn't exsist in the keys we create above then add it to the end of the dictionary. This should just maybe do a "'6': set()" for expample ^set command
        self.vertices[node] = set()
        print(self.vertices)

    def add_edge(self, node, edge):
        if node in self.vertices:
            self.vertices[node].add(edge) 
        else:
            raise Exception("you done goof'd")

        if edge in self.vertices:
            self.vertices[edge].add(node)
        else:
            raise Exception("you done goof'd")
        
# if key exsists then somehow change the values to reflect the connection between the two nodes. ^Add *add to both 
# counter = -1

increment = counterCreator()

class Vertex:
    def __init__(self, name=increment()):
        self.name = name    # 0
        self.edges = set()  # a set to all other vertices it's connected to

    def add_edge(self, vertex):
        self.edges.add(vertex)

some_vertex = Vertex('0')
"""
some_vertex = {
    name: '0',
    edges: {'1', '5'}
}
"""


    
# This represents a graph with five vertices and three total (bidirectional) edges. 
# The vertex '0' and 2' have no edges, while '1' is connected to both '4' and '5', and '3' is connected to '4'.

graph = Graph()
graph.add_vertex(some_vertex)
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_edge('1', '4')
graph.add_edge('1', '5')
graph.add_edge('3', '4')
# graph.add_edge('7', '4')
print(graph.vertices)

# test_vertices = {
#         '0': set(),
#         '1': {'4', '5'},
#         '2': set(),
#         '3': {'4'},
#         '4': {'1','3'},
#         '5': {'1'},
#         '6': set()
# }