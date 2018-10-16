"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
# if key doesn't exsist in the keys we create above then add it to the end of the dictionary. This should just maybe do a "'6': set()" for expample ^set command
        if vertex.name in self.vertices:
            raise Exception("ALREADY EXSISTS!")

        self.vertices[vertex.name] = vertex
        # pass

    def add_edge(self, vert1, vert2):
        """
        vert1 and vert 2 are a vertex object
        gives both vertices a bidirectional edge
        vert1 and vert2 has an `add_edge` method
        """
        vert1.add_edge(vert2)
        vert2.add_edge(vert1)
        
        
# if key exsists then somehow change the values to reflect the connection between the two nodes. ^Add *add to both 
# counter = -1

class Vertex:
    def __init__(self, name):
        self.name = str(name)    # 0
        self.edges = set()  # a set to all other vertices it's connected to

    def __eq__(self, other):
        return self.name == str(other) 

    def add_edge(self, vertex):
        self.edges.add(vertex)

    def get_edges(self):
        print(f"Edges for vertex {self.name}")
        for edge in self.edges:
            print(edge)

    def __repr__(self):
        return f"{self.name}"
# some_vertex = Vertex('0')
"""
some_vertex = {
    name: '0',
    edges: {'1', '5'}
}

"""


    
# This represents a graph with five vertices and three total (bidirectional) edges. 
# The vertex '0' and 2' have no edges, while '1' is connected to both '4' and '5', and '3' is connected to '4'.

if __name__ == '__main__':
    # graph = Graph()
    # # graph.add_vertex(some_vertex)
    # graph.add_vertex('1')
    # graph.add_vertex('2')
    # graph.add_vertex('3')
    # graph.add_vertex('4')
    # graph.add_vertex('5')
    # graph.add_edge('1', '4')
    # # graph.add_edge(some_vertex, another_vertex)
    # graph.add_edge('1', '5')
    # graph.add_edge('3', '4')
    # # graph.add_edge('7', '4')
    # print(graph.vertices)

    graph = Graph()
    vertex_list = []
    for i in range(6):
        vertex_list.append(Vertex(i))

    # vertex_list.append(Vertex('4'))

    for vertex in vertex_list:
        graph.add_vertex(vertex)
    
    graph.add_edge(vertex_list[0], vertex_list[1])
    graph.add_edge(vertex_list[0], vertex_list[2])
    graph.add_edge(vertex_list[3], vertex_list[5])

    # print('vertex: 0', vertex_list[0])
    # print('vertex: 3', vertex_list[3])
    vertex_list[0].get_edges()
    vertex_list[1].get_edges()
    vertex_list[2].get_edges()
    vertex_list[3].get_edges()
    vertex_list[5].get_edges()
    # print(graph.vertices)


# test_vertices = {
#         '0': set(),
#         '1': {'4', '5'},
#         '2': set(),
#         '3': {'4'},
#         '4': {'1','3'},
#         '5': {'1'},
#         '6': set()
# }