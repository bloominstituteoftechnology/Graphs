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


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


def earliest_ancestor(ancestors, starting_node):
    grand_parents = {}
    for ancestor in ancestors:
        if ancestor[1] not in grand_parents:
            grand_parents[ancestor[1]] = set()
        grand_parents[ancestor[1]].add(ancestor[0])
    if starting_node not in grand_parents:
        return -1
    stack = Stack()
    visited = []
    original = []
    stack.push([starting_node])
    while stack.size() > 0:
        path = stack.pop()
        node = path[-1]
        if node not in visited:
            visited.append(node)
            if len(path) > len(original):
                original = path
            if len(path) == len(original) and path[-1] < original[-1]:
                original = path

            if node in grand_parents:
                for parent in grand_parents[node]:
                    new_path = path[:]
                    new_path.append(parent)
                    stack.push(new_path)

    return original[-1]

    print(grand_parents)


earliest_ancestor(test_ancestors, None)
