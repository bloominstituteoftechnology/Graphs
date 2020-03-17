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

    """Represent a graph as a dictionary of vertices mapping
    labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")


def earliest_ancestor(ancestors, starting_node):
    # Build our graph
    graph = Graph()

    # Add vertex pairs to graph
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        # build edges in reverse, so the parent is not aware
        # of the child
        graph.add_edge(pair[1], pair[0])

    # Create queue and enqueue starting_node
    q = Queue()
    q.enqueue([starting_node])

    max_path_length = 1
    earliest_ancestor = -1

    # While queue is not empty
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if (len(path) >= max_path_length and v < earliest_ancestor) or (len(path) > max_path_length):
            earliest_ancestor = v
            max_path_length = len(path)

        for neighbor in graph.vertices[v]:
            new_path = list(path)
            new_path.append(neighbor)
            q.enqueue(new_path)

    return earliest_ancestor
