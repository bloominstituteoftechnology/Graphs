# import random

# class Vertex:
#     def __init__(self, label, color="gray", **pos):
#         self.label = label
#         self.color = color
#         self.pos = pos
#         self.edges = set()

#     '''
#     def __repr__(self):
#         return str(self.label)
#     '''

#     # Use the str method instead
#     def __str__(self):
#         if not self.pos:
#             pos = dict(x=None, y=None)
#         else:
#             pos = self.pos
#         return "Vartex is {}, position at ({}, {}), color is {} and has edges  {}".format(self.label, pos['x'], pos['y'], self.color, self.edges)

# class Graph:
#     def __init__(self):
#         self.vertices = {}
#         self.nodes = set()
#         #Each edge will have a "weight" repseanted by distance.
#         self.distance = {}
#         self.edges = defaultdict(list)

#     # we can see what properties are on the Graph
#     def __str__(self):
#         return str(self.vertices)

#     def add_edge(self, start, end, bidirectional=True):
#         """ And an edge (default bidirectional) between two vertices"""

#         # Change this so that if not in vertices, just add it
#         '''
#         if start not in self.vertices or end not in self.vertices:
#             raise Exception("Vertices to connect not in graph!")
#         self.vertices[start].add(end)
#         '''
#         # using the key, if we are passed an object just get the key

#         if isinstance(start, Vertex):
#             start = start.label

#         if isinstance(end, Vertex):
#             end = end.label

#         # add start if not in vertices
#         if start not in list(self.vertices.keys()):
#             self.add_vertex(Vertex(start))

#         # add end if not in vertices
#         if end not in list(self.vertices.keys()):
#             self.add_vertex(Vertex(end))

#         self.vertices[start].edges.add(self.vertices[end])
#         if bidirectional:
#             self.vertices[end].edges.add(self.vertices[start])

#     def add_vertex(self, vertex):

#         if not isinstance(vertex, Vertex):
#             vertex = Vertex(vertex)

#         if vertex.label in self.vertices:
#             return False  # ignores it

#         self.vertices[vertex.label] = vertex
#         return True  # added

#     # Create a random graph
#     def create_vertices_and_edges(self, n_verts):
#         # create verts and put them in a grid
#         grid = []
#         for i in range(n_verts):
#             grid.append(Vertex(str(i)))
#         for i in range(n_verts - 1):
#             if (random.randrange(n_verts) < n_verts // 2):
#                 if(random.randrange(n_verts) < n_verts // 2):
#                     self.add_edge(grid[i].label, grid[i+1].label, False)
#                 self.add_edge(grid[i].label, grid[i+1].label)

#         for vert in grid:
#             self.add_vertex(vert)

#     # for debugging only

#     def debug_create_test_data(self):

#         v0 = Vertex("0")
#         self.add_vertex(v0)
#         self.add_vertex("1")
#         self.add_vertex("2")
#         self.add_vertex("3")
#         self.add_vertex("4")
#         self.add_vertex("5")
#         self.add_vertex("6")
#         self.add_vertex("7")
#         self.add_vertex("8")
#         self.add_vertex("9")
#         self.add_vertex("10")

#         self.add_edge("0", "1")
#         self.add_edge("5", "1")
#         self.add_edge("7", "5", False)

#     def bfs(self, start):
#         random_color = '#' + \
#             ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
#         queue = []
#         found = []
#         queue.append(start)
#         found.append(start)

#         start.color = random_color

#         while (len(queue) > 0):
#             v = queue[0]
#             for edge in v.edges:
#                 if edge not in found:
#                     found.append(edge)
#                     queue.append(edge)
#                     edge.color = random_color

#             queue.pop(0)
#         return found

#     # Get the connected components
#     def get_connected_components(self):

#         searched = []

#         for index, vertex in self.vertices.items():
#             if vertex not in searched:
#                 searched.append(self.bfs(vertex))

#         return searched

from decimal import Decimal

class Node:
    def __init__(self, label):
        self.label = label

class Edge:
    def __init__(self, to_node, length):
        self.to_node = to_node
        self.length = length

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = dict()

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, length):
        edge = Edge(to_node, length)
        if from_node.label in self.edges:
            from_node_edges = self.edges[from_node.label]
        else:
            self.edges[from_node.label] = dict()
            from_node_edges = self.edges[from_node.label]
        from_node_edges[to_node.label] = edge

def min_dist(q, dist):
    """
    Returns the node with the smallest distance in q.
    Implemented to keep the main algorithm clean.
    """
    min_node = None
    for node in q:
        if min_node == None:
            min_node = node
        elif dist[node] < dist[min_node]:
            min_node = node

    return min_node

AnswerToTheUniverse = Decimal('Infinity')

def dijkstra(graph, source):
    q = set()
    dist = {}
    prev = {}

    for v in graph.nodes:                   # initialization
        dist[v] = AnswerToTheUniverse       # unknown distance from source to v
        prev[v] = AnswerToTheUniverse       # previous node in optimal path from source
        q.add(v)                            # all nodes initially in q (unvisited nodes)

    # distance from source to source
    dist[source] = 0

    while q:
        # node with the least distance selected first
        u = min_dist(q, dist)

        q.remove(u)

        if u.label in graph.edges:
            for _, v in graph.edges[u.label].items():
                alt = dist[u] + v.length
                if alt < dist[v.to_node]:
                    # a shorter path to v has been found
                    dist[v.to_node] = alt
                    prev[v.to_node] = u

    return dist, prev


def to_array(prev, from_node):
    """Creates an ordered list of labels as a route."""
    previous_node = prev[from_node]
    route = [from_node.label]
    while previous_node != AnswerToTheUniverse:
        route.append(previous_node.label)
        temp = previous_node
        previous_node = prev[temp]

    route.reverse()
    return route

graph = Graph()
node_a = Node("A")
graph.add_node(node_a)
node_b = Node("B")
graph.add_node(node_b)
node_c = Node("C")
graph.add_node(node_c)
node_d = Node("D")
graph.add_node(node_d)
node_e = Node("E")
graph.add_node(node_e)
node_f = Node("F")
graph.add_node(node_f)
node_g = Node("G")
graph.add_node(node_g)

graph.add_edge(node_a, node_b, 4)
graph.add_edge(node_a, node_c, 3)
graph.add_edge(node_a, node_e, 7)
graph.add_edge(node_b, node_c, 6)
graph.add_edge(node_b, node_d, 5)
graph.add_edge(node_c, node_d, 11)
graph.add_edge(node_c, node_e, 8)
graph.add_edge(node_d, node_e, 2)
graph.add_edge(node_d, node_f, 2)
graph.add_edge(node_d, node_g, 10)
graph.add_edge(node_e, node_g, 5)
graph.add_edge(node_f, node_g, 3)

dist, prev = dijkstra(graph, node_a)

print("The quickest path from {} to {} is [{}] with a distance of {}".format(
    node_a.label,
    node_f.label,
    " -> ".join(to_array(prev, node_f)),
    str(dist[node_f])
    )
)

#Thank to https://gist.github.com/econchick . I would not have understand half of this or even what a shortest path is without his gists and explanation. 