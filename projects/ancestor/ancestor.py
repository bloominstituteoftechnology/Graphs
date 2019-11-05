class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


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
        self.vertices[v2].add(v1)

    def is_vertex(self, value):
        return value in self.vertices

    def dfs(self, starting_vertex):
        s = Stack()
        # make a visited set
        visited = set()
        # push on the stack the PATH to that node
        s.push([starting_vertex])
        # define empty list to store the final path that crops up
        last_path = []
        # while the queue isn't empty:
        while s.size() > 0:
            # pop the PATH
            path = s.pop()
            # the last thing in the path is our current item
            node = path[-1]  # -1 in python is the end of the list
            # if it's not visited:
            if node not in visited:
                # for each of the node's neighbor's
                for neighbor in self.vertices[node]:
                    # copy the path
                    # slicing the entire list works too - path[:]
                    copy_path = path.copy()
                    # add the neighbor to the path
                    copy_path.append(neighbor)
                    # enqueue the PATH_COPY
                    s.push(copy_path)

        parent = float('-inf')
        max_path_length = float('inf')

        for path in last_path:
            if len(path) > max_path_length:
                max_path_length = len(path)
                parent = path[-1]

            if len(path) == max_path_length:
                parent = min(parent, path[-1])

        if parent == starting_vertex:
            parent = -1

        return parent


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for relationship in ancestors:
        if not graph.is_vertex(relationship[0]):
            graph.add_vertex(relationship[0])

        if not graph.is_vertex(relationship[1]):
            graph.add_vertex(relationship[1])

        graph.add_edge(relationship[1], relationship[0])

    return graph.dfs(starting_node)
