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
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_parent(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_parents(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return -1

    def earliest(self, starting_node):
        q = Queue()
        q.enqueue([starting_node])
        paths = []
        visited = set()
        while q.size() > 0:
            path = q.dequeue()
            current_node = path[-1]
            if self.get_parents(current_node) == -1:
                paths.append(path)
            if current_node not in visited:
                if self.get_parents(current_node) != -1:
                    parents = self.get_parents(current_node)
                    for parent in parents:
                        next_path = path + [parent]
                        q.enqueue(next_path)
        return paths


def earliest_ancestor(ancestors, starting_node):
    parents = Graph()
    for ancestor in ancestors:
        parents.add_vertex(ancestor[1])
    for ancestor in ancestors:
        parents.add_parent(ancestor[1], ancestor[0])
    if parents.get_parents(starting_node) == -1:
        return -1
    paths = parents.earliest(starting_node)
    longest_path = paths[0]
    for path in paths:
        if len(path) == len(longest_path):
            if path[-1] < longest_path[-1]:
                longest_path = path
        if len(path) > len(longest_path):
            longest_path = path
    return(longest_path[-1])


earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                   (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 6)
