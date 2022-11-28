"""
Plan:
Build Graph, or just define get_neighbors
Choose Alogrithm --> DFS

"""

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


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

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex):
        return self.vertices[vertex]
# build a path
# when don't know when to stop until all nodes are visited, so BFS maybe the best option


def build_graph(ancestors):
    graph = Graph()
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
    return graph


def earliest_ancestor(ancestors, starting_node):
    graph = build_graph(ancestors)
    s = Stack()
    visited = set()

    s.push([starting_node])

    longest_path = []
    aged_one = -1

    while s.size():
        path = s.pop()
        cur_node = path[-1]

        if (len(path) > len(longest_path)) or (len(path) == len(longest_path)) and cur_node < aged_one:
            # makes the current path the longest path
            longest_path = path
            # if no ancestor
            aged_one = longest_path[-1]

        if cur_node not in visited:
            visited.add(cur_node)

            parents = graph.get_neighbors(cur_node)
            for parent in parents:
                new_path = path + [parent]
                s.push(new_path)
    if len(longest_path) == 1:
        return -1
    else:
        return longest_path[-1]


print(earliest_ancestor(test_ancestors, 2))
print(earliest_ancestor(test_ancestors, 1))
print(earliest_ancestor(test_ancestors, 6))
