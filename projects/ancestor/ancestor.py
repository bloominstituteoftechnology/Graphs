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
    def __init__(self):
        self.vertices = {}

    def add_vertices(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex):
        return self.vertices[vertex]


def make_graph(ancestors):
    graph = Graph()
    for parent, child in ancestors:
        graph.add_vertices(parent)
        graph.add_vertices(child)
        graph.add_edge(child, parent)
    return graph


def earliest_ancestor(ancestors, starting_node): 
    graph = make_graph(ancestors)

    s = Stack()
    visited = set()
    s.push([starting_node])
    longest_path = []

    while s.size() > 0:
        path = s.pop()
        current_node = path[-1]

        if len(path) > len(longest_path):
            longest_path = path

        if current_node not in visited:
            visited.add(current_node)
            parents = graph.get_neighbors(current_node)

            for parent in parents:
                new_path = path+[parent]
                s.push(new_path)
    if starting_node == longest_path[-1]:
        return -1
    else:
        return longest_path[-1]
