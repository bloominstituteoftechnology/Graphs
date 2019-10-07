class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}


    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)

        self.vertices[v1].add(v2)


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    # Add the edges
    for group in ancestors:
        pair = list(group)
        graph.add_edge(pair[1], pair[0])

    # Use BFT
    queue = []
    bft_path = []
    highest_nodes = []
    visited = set()

    queue.append(starting_node)
    highest_nodes.append(starting_node)
    visited.add(starting_node)

    index = len(highest_nodes)
    count = len(highest_nodes)

    while True:
        # Dequeue the first value in the queue
        node = queue.pop(0)
        bft_path.append(node)

        # Add current node's parents to highest nodes
        highest_nodes += list(graph.vertices[node])

        # Break out of the loop when the queue is empty and current node has no parents
        if not len(queue) and not graph.vertices[node]:
            break

        count -= 1

        # If count = 0, modify highest nodes to contain all nodes only in highest level
        if not count:
            highest_nodes = highest_nodes[index:]
            count = len(highest_nodes)
            index = len(highest_nodes)

        for parent in graph.vertices[node]:
            if parent not in visited:
                queue.append(parent)
                visited.add(parent)

    if highest_nodes[0] == starting_node:
        return -1
    else:
        return min(highest_nodes)