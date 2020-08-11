class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph():
    def __init__(self):
        self.vertices = {}

    def add_vertex(self,vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].add(vertex2)

# This will be similar to depth first
# def earliest_ancestor(ancestors, starting_node):
#     # build the graph
#     g = Graph()

#     # Add the parents
#     for parent in ancestors:
#         g.add_vertex(parent[0])
#         g.add_vertex(parent[1])

#         # add in the edge
#         g.add_edge(parent[0], parent[1])

#     # start the queue to handle the path
#     q = Queue()
#     q.enqueue([starting_node])

#     # initialize with -1 for no neighbors
#     longest_path = 1
#     earliest = -1

#     while q.size() > 0:
#         path = q.dequeue()
#         last_vertex = path[-1]

#         if (len(path) >= longest_path and last_vertex < earliest) or \
#             (len(path) > longest_path):
#             earliest = last_vertex
#             longest_path = len(path)
#         # look at neighbors
#         for next_item in g.vertices[last_vertex]:
#             path_copy = list(path)
#             path_copy.append(next_item)
#             q.enqueue(path_copy)
#     return earliest

