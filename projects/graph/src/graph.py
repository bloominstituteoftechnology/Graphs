"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
# if key doesn't exsist in the keys we create above then add it to the end of the dictionary. This should just maybe do a "'6': set()" for expample ^set command
        if name in self.vertices:
            raise Exception("ALREADY EXSISTS!")

        self.vertices[name] = Vertex(name)
        # pass

    def add_edge(self, str1, str2, bidirectional=True):
        """
        add_edge accepts:
        str1 (string)
        str2 (string)
        bidirectional (boolean) (default: True)
        Creates an edge between two vertices. Bidirectional flag controls
        if edges are undirected or directed. Will throw error if any of
        the vertices do not exist.
        """
        print('self.vertices:', self.vertices)
        if str1 not in self.vertices:
            raise Exception(f"Vertex {str1} does not exist")
        if str2 not in self.vertices:
            raise Exception(f"Vertex {str2} does not exist")
        self.vertices[str1].add_edge(str2)
        if bidirectional:
            self.vertices[str2].add_edge(str1)
        # graph.add_vertex('a')
        # {
        #     'a': <Vertex Object at 0xFFFFF69696969>
        #     # "a": "{'b', 'c'}"
        # }
        
# if key exsists then somehow change the values to reflect the connection between the two nodes. ^Add *add to both 
# counter = -1

class Vertex:
    def __init__(self, name, x=None, y=None):
        self.name = str(name)    # 0
        self.edges = set()  # a set to all other vertices it's connected to
        if x == None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y == None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y

    """
    The below __eq__ method probably needs to be paired with __hash__ to work properly, but what all this stuff 
    even does is starting to go beyond my head. More research needed.
    """
    # TODO: Implement equality and hash methods so python can evaluate equality between vertex objects 
    # def __eq__(self, other):
    #     return self.name == str(other) 
    # def __hash__(self):
    #     pass
    def add_edge(self, vertex):
        self.edges.add(vertex)

    def get_edges(self):
        # print(f"Edges for vertex {self.name}")
        # for edge in self.edges:
        #     print(edge)
        return self.edges

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
    """
    Which test is failing?
    """
    for vertex in vertex_list:
        graph.add_vertex(vertex)
    
    graph.add_edge(vertex_list[0], vertex_list[1]) #this one maybe

    # """
    #     C:\Users\aReJay\Lambda\Graphs\projects\graph\src>python graph.py
    #     Traceback (most recent call last):
    #     File "graph.py", line 90, in <module>
    #     graph.add_edge(vertex_list[0], vertex_list[1])
    #       File "graph.py", line 24, in add_edge
    #         vert1.add_edge(vert2)
    #      File "graph.py", line 40, in add_edge
    #     self.edges.add(vertex)
    #      TypeError: unhashable type: 'Vertex'
    # """
    # Thinking about it. We didn't have this issue yesterday, did we?
    graph.add_edge(vertex_list[0], vertex_list[2])
    graph.add_edge(vertex_list[3], vertex_list[5])

    # print('vertex: 0', vertex_list[0])
    # print('vertex: 3', vertex_list[3])
    print(vertex_list[0].get_edges())
    print(vertex_list[1].get_edges())
    print(vertex_list[2].get_edges())
    print(vertex_list[3].get_edges())
    print(vertex_list[5].get_edges()) #there shouldn't be any errors here :thinkingface:
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