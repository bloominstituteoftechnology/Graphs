class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
 

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    q = Queue()
    
    q.enqueue([starting_node])
    max_length = 1
    earliest = -1

    for pair in ancestors:
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])
        g.add_edge(pair[1], pair[0])

    while q.size() > 0:
        path = q.dequeue()
        curr = path[-1]

        if len(path) > max_length:
            max_length = len(path)
            earliest = curr
        elif len(path) == max_length:
            if curr < earliest:
                earliest = curr

        for neighbor in g.get_neighbors(curr):
            q.enqueue(path + [neighbor])

    return earliest 