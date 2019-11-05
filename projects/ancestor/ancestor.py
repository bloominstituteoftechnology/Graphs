from util import Stack

def earliest_ancestor(ancestors, starting_node):
    visited = {}
    length = 0
    longest_path =[]
    path = [ancestors[0][0]]
    s = Stack()
    s.push(path)
    while s.size():
        path = s.pop()
        node = path[-1]
        if node == starting_node:
            if len(path) > len(longest_path):
                longest_path = path
        if node not in visited:
            visited[node] = path
            for neighbor in ancestors[node]:
                path_copy = path[:]
                path_copy.append(neighbor)
                s.push(path_copy)
    return longest_path[0]
    pass