class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """

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
        If both exist add a connection from v1 to v2
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist!')


class Queue:
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


def earliest_ancestor(ancestors, starting_node):
    # Create graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # Create reverse path edges
        graph.add_edge(pair[1], pair[0])
    # Establish placeholder for longest path
    max_path_len = 1
    # Establish place holder for oldest_ancestor
    earliest_ancestor = -1
    # Use BFS to store the path
    queue = Queue()
    queue.enqueue([starting_node])
    # While loop for existing nodes in queue
    while queue.size() > 0:
        # remove fist node
        path = queue.dequeue()
        # Get the last item in the current node
        vertex = path[-1]
        # If length of family is >= and the value is <, or if the length of family is longer
        if (len(path) >= max_path_len and vertex < earliest_ancestor) or (len(path) > max_path_len):
            # Updating earliest to curr_node
            earliest_ancestor = vertex
            # Updating curr_size
            max_path_len = len(path)
            # Traversing parents
        for neighbor in graph.vertices[vertex]:
            # Make family copy
            path_copy = list(path)
            # Append curr_node to copy of family
            path_copy.append(neighbor)
            # Enqueue to family copy
            queue.enqueue(path_copy)

    return earliest_ancestor
