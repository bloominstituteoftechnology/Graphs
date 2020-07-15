from projects/graph/util import Stack, Queue
from prjects/graph/graph import Graph



def earliest_ancestor(ancestors, starting_node):
    # for this we want a reversed DFS
    visited = set()
    s = Stack()
    s.push([starting_node])

    while s.size() > 0:
        path = s.pop()

        v = path[-1]

        if v not in visited:
            visited.add(v)

            if v == end_word:
                return path

            for parents in get_parents(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                s.push(path_copy)







test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 2))