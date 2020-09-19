from collections import deque

def earliest_ancestor(ancestors, starting_node):
    if len(ancestors) == 0:
        return "empty list"
    graph = create_graph(ancestors)
    stack = deque()
    visted = set()
    print(graph)
    print(starting_node)

def create_graph(ancestors):
    graph = {}
    for parent, child in ancestors:
        if parent in graph:
            graph[parent].add(child)
        else:
            graph[parent] = {child}
    return graph

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 6)