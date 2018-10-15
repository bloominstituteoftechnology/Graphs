"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex in self.vertices:
            raise Exception('Error: this vertex already exists')
        self.vertices[vertex] = set()

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error - vertices not in graph!')
        self.vertices[start].add(end)
        self.vertices[end].add(start)

# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self):
#         self.vertices = {}
    
#     def add_vertex(self, vertex_id, color='red'):
#         # if vertex in self.vertices:
#         #     raise Exception('Error: this vertex already exists')
#         self.vertices[vertex_id] = Vertex(vertex_id, f"V_{vertex_id}", color)
#     def get_edges(self, vertex_id):
#         self.vertices[vertex_id]
#     def add_edge(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#             self.vertices[v2].add(v1)
#         else:
#             raise Exception('That vertex does not exists.')
#     def add__directed_edge(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#         else:
#             raise Exception('That vertex does not exists.')

    # """ lecture sol """
    # def add_vertex(self, vertex, edges=()):
    #     # we don't want to have mutable values as default arguments such as edges=set() or edges=[];
    #     # edges = () tuples are immutable, so they are safe to have as default argument
    #     if vertex in self.vertices:
    #         raise Exception('Error: adding vertex that already exists')
    #     if not set(edges).issubset(self.vertices):
    #         raise Exception('Error: cannot have edge to nonexistent vertices')
    #     self.vertices[vertex] = set(edges)

    # def add_edge(self, start, end, bidirectional=True):
    #     """Add a edge (default bidirectional) between two vertices."""
    #     if start not in self.vertices or end not in self.vertices:
    #         raise Exception('Error - vertices not in graph!')
    #     self.vertices[start].add(end)
    #     if bidirectional:
    #         self.vertices[end].add(start)

# class Vertex:
#     def __init__(self, vertex_id, value, color='green')
#         self.id=vertex_id
#         self.value=value
#         self.color=color
#         self.edges=[]


# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# # graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# graph.add_edge('1', '2')
# graph.add_edge('0', '4')
# print(len(graph.vertices))
# print(graph.vertices)

def dft(adjList, node_id, visited):
    print(node_id)
    visited.append(node_id)
    for el in adjList[node_id]:
        if el not in visited:
            dft(adjList, el, visited)

# def dft(adjList, node_id, visited, search_node):
#     if node_id == search_node: 
#         return true
#     visited.append(node_id)
#     for el in adjList[node_id]:
#         if el not in visited:
#             dft(adjList, el, visited, search_node)
#         return false
def bft(aList, node_id):
    arr = []
    arr.append(node_id)
    visited = []
    while len(frontier) > 0:
        n = frontier.pop()
        if n not in visited:
            print(n)
            visited.append(n)
            for el in aList[n]:
                arr.append(el)

