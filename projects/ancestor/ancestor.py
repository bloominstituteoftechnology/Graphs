
# Our Nodes will be numbers and our edges will appear when a child has a parent
# build our graph and define get neighbors method
# Use breadth first/DF to visit all nodes
# build a path like in a search

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
                s.push(path+[parent])

    if starting_node == longest_path[-1]:
        return -1
    else:
        return longest_path[-1]


l = make_graph([(1, 3), (2, 3), (3, 6), (5, 6),
                (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)])
print(l.vertices)
# def earliest_ancestor(ancestors, starting_node):
#
#     famtree = dict()

#
#     for ancestor in ancestors:
#         kid = ancestor[1]
#         if kid not in famtree:
#             famtree[kid] = set()
#             famtree[kid].add(ancestor[0])

#         else:
#             famtree[kid].add(ancestor[0])

#     kids = list(famtree.keys())

#     parents = set()
#     for ancestor in ancestors:
#         parents.add(ancestor[0])
#     parents = list(parents)

#     if starting_node not in kids:
#         return -1

#     s = list()
#     s.append(starting_node)

#     seen = set()
#     rents_ids = list()
#     path = list()

#     while len(s) > 0:
#         # Sorting s forces the smallest value on any particular traversed level to go last
#         s.sort()
#         current = s.pop()

#         if current not in seen:
#             seen.add(current)
#             path.append(current)

#             if current in kids:
#                 rents_ids = list(famtree[current])
#                 for ids in rents_ids:
#                     s.append(ids)
#     return path[-1]
