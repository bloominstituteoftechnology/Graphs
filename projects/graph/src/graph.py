"""
Simple graph implementation compatible with BokehGraph class.
"""
# class Vertex:
#     def __init__(self, n):
#         self.name = n
#         self.children = list()

#     def add_child(self, v):
#         if v not in self.children:
#             self.children.append(v)
#             self.children.sort()


# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""

#     def __init__(self):
#         self.vertices = {}

#     def add_vertex(self, vertex):
#         if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
#             self.vertices[vertex.name] = vertex
#             return True
#         else:
#             return False

#     def add_edge(self, u, v):
#         if u in self.vertices and v in self.vertices:
#             for key, value in self.vertices.items():
#                 if key == u:
#                     value.add_child(v)
#                 if key == v:
#                     value.add_child(u)
#             return True
#         else:
#             return False

#     def print_graph(self):
#         for key in sorted(list(self.vertices.keys())):
#             print(key + str(self.vertices[key].children))


# g = Graph()
# a = Vertex('A')
# g.add_vertex(a)
# g.add_vertex(Vertex('B'))

# for i in range(ord('A'), ord('K')):
#     g.add_vertex(Vertex(chr(i)))

# edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH',
#          'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
# for edge in edges:
#     g.add_edge(edge[:1], edge[1:])

# g.print_graph()

"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exist")

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def bft(self, start):
        q = Queue()
        visited = set()
        q.enqueue(start)
        while q.size() > 0:
            node = q.dequeue()
            if node not in visited:
                print(node)
                visited.add(node)
                for child in self.vertices[node].edges:
                    if child not in visited:
                        q.enqueue(child)


class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.edges = set()


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if(self.size()) > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)
