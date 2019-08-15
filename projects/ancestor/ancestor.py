from collections import defaultdict


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


def dfs(starting_vertex, family):
    visited = []
    s = Stack()
    s.push([starting_vertex])
    while s.size() > 0:
        path = s.pop()
        v = path[-1]
        if v not in visited:
            visited.append(v)
        for neighbor in family[v]:
            path_copy = [*path]
            path_copy.append(neighbor)
            s.push(path_copy)
    return visited[-1]


def earliest_ancestor(dataset, individual):
    family = defaultdict(list)
    for parent, child in dataset:
        family[child].append(parent)
    if individual not in family:
        return -1
    ancestor = dfs(individual, family)
    return ancestor

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 4)]
ancestors = []
for child, parent in test_ancestors:
    ancestors.append((parent, child))

for i in range(1, 12):
    print(i, earliest_ancestor(ancestors, i))
