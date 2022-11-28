from collections import deque

def earliest_ancestor(ancestors, starting_node):
    vertices = {}
    # Take ancestor data and convert to graph
    # children -> parent, but not visa versa
    for parent, child in ancestors:
        if child not in vertices:
            vertices[child] = set()
            vertices[child].add(parent)
            if parent not in vertices:
                vertices[parent] = set()
        else:
            vertices[child].add(parent)
            if parent not in vertices:
                vertices[parent] = set()

    # No parents, return -1
    if len(vertices[starting_node]) == 0:
        return -1

    # Only interested in terminal nodes (parents), and I want to know what 
    # generation they belong to.
    stack = deque()
    early_gen = 0
    stack.append((starting_node, 0))
    terminal = {}
    while len(stack) > 0:
        curr_vertex, curr_gen = stack.pop()

        if curr_gen > early_gen:
            early_gen = curr_gen

        if len(vertices[curr_vertex]) == 0:
            terminal[curr_gen] = terminal.get(curr_gen, [])
            terminal[curr_gen].append(curr_vertex)

        for parent in vertices[curr_vertex]:
            stack.append((parent, curr_gen + 1))

    terminal[early_gen].sort()
    return terminal[early_gen][0]
