"""
Simple graph implementation compatible with BokehGraph class.
"""
# http://interactivepython.org/courselib/static/pythonds/Graphs/Implementation.html
# https://www.python.org/doc/essays/graphs/
# https://www.programiz.com/python-programming/methods/built-in/hash
# https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/

# the vertex class will create a single object with a key and an attached array of connections
    # vertex = {'A': ['B', 'C']}


# the Graph Class should create an object with vertices, each of which has a corresponding collection of neighbors
    # graph = {'A': ['B', 'C'],
    #          'B': ['C', 'D'],
    #          'C': ['D'],
    #          'D': ['C'],
    #          'E': ['F'],
    #          'F': ['C']}

class Vertex:
    def __init__(self, key):
        # storage space for neighboring nodes
        self.id = id
        self.neighbors = []

    # method to retrieve the key associated with a vertex
    def __repr__(self):
        return str(self.key)

    # method to access the key associated with the vertex
    def __hash__(self):
        return hash(str(self.key))

    # method to check the key on a vertex, returns True if equal
    def __equal__(self, input):
        return self.key == str(input)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.vertCount = 0

    def add_vertex(self, vertex, edges = ()):
        if vertex in self.vertices:
        #  https://realpython.com/python-exceptions/            
            raise Exception('Error: that vertex already exists')
            # https://www.programiz.com/python-programming/methods/set/issubset
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: that vertex does not exist')
            #https://docs.python.org/2/library/sets.html
        self.vertices[vertex] = set(edges)
    
    def get_vertex(self,n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None
    
    def __contains__(self,n):
        return n in self.vertices

    def add_edge(self, start, end, bothWays = True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('These vertices are not in the graph')
        self.vertices[start].add(end)
        if bothWays:
            self.vertices[end].add(start)

    def vertices(self):
        return self.vertices.keys()


# Tests for Graph Class
graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('1', '2')
graph.add_edge('1', '4')
print(graph.vertices)


