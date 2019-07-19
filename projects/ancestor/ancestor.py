
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

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


def earliest_ancestor(ancestors, starting_node):
    family_connections = {}
    for ancestor in ancestors:
        if ancestor[1] not in family_connections:
            family_connections[ancestor[1]] = set()
        family_connections[ancestor[1]].add(ancestor[0])

    if starting_node not in family_connections:
        print(-1)
        return -1
    oldest = []
    earliest = Stack()
    visited = []

    earliest.push([starting_node])

    while earliest.size():
        path = earliest.pop()
        node = path[-1]
        if node not in visited:
            visited.append(node)
            if len(path) > len(oldest):
                oldest = path
            if len(path) == len(oldest) and path[-1] < oldest[-1]:
                oldest = path

            
            if node in family_connections:
                for neighbor in family_connections[node]:
                    new_path = path[:]
                    new_path.append(neighbor)

                    earliest.push(new_path)

    print(oldest[-1])
    return oldest[-1]    



earliest_ancestor(test_ancestors, 6)