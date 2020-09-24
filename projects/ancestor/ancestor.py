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
    def __init__(self):
        self.vertices = {}
        self.visited = set()

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, vert_1, vert_2):
        if vert_1 in self.vertices and vert_2 in self.vertices:
            self.vertices[vert_1].add(vert_2)
        else:
            raise IndexError("Cannt create edge with those vertices... sorry.")

    def get_neighbor(self, vertex_id):
        return self.vertices[vertex_id] if vertex_id in self.vertices else set()


def earliest_ancestor(ancestors, starting_node):
    new_graph = Graph()

    for pair in ancestors:
        new_graph.add_vertex(pair[0])
        new_graph.add_vertex(pair[1])
        new_graph.add_edge(pair[1], pair[0])

    queue = Queue()
    queue.enqueue([starting_node])
    max_length = 1
    earliest = -1

    while queue.size() > 0:
        vert = queue.dequeue()
        curr = vert[-1]

        if len(vert) > max_length:
            max_length = len(vert)
            earliest = curr
        elif len(vert) == max_length:
            if curr < earliest:
                earliest = curr

        for neighbor in new_graph.get_neighbor(curr):
            print("v: ", vert, "n: ", neighbor)
            queue.enqueue(vert + [neighbor])

    return earliest
