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

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):
    ancestors_graph = Graph()
    for pair in ancestors:
        ancestors_graph.add_vertex(pair[0])
        ancestors_graph.add_vertex(pair[1])
        ancestors_graph.add_edge(pair[1], pair[0]) #bfs storing the path of how you get to the first instance of the earliest ancestor
    queue = Queue()
    queue.enqueue([starting_node])
    max_path_length = 1
    earliest = -1

    while queue.size() > 0:
        v = queue.dequeue()
        curr = v[-1]

        if len(v) > max_path_length:
            max_path_length = len(v)
            earliest = curr
        elif len(v) ==  max_path_length:
            if curr < earliest:
                earliest = curr

        for neighbor in ancestors_graph.get_neighbors(curr):
            queue.enqueue(v + [neighbor])

    return earliest