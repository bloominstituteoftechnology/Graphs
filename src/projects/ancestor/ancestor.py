from collections import deque

def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    graph = {}

    for pair in ancestors:
        graph[]
        graph.add_vertex(pair[1])
        # Build edges in reverse
        graph.add_edge(pair[1], pair[0])

    # Do a BFS (storing the path)
    q = deque()
    q.enqueue([starting_node])
    max_path_len = 1
    early_ancestor = -1

    while q:
        path = q.dequeue()
        v = path[-1]
        # If the path is longer or equal and the value is smaller, or if the path is longer)
        if (len(path) >= max_path_len and v < early_ancestor) or (len(path) > max_path_len):
            early_ancestor = v
            max_path_len = len(path)

        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)

    return early_ancestor

# def earliest_ancestor(ancestor, starting_nodes):
#     graph = {}
#     for node, connection in ancestor:
#
#         if node in graph:
#             graph[node].add(connection)


if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    earliest_ancestor(test_ancestors)
