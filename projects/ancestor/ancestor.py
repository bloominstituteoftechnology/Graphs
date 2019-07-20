test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestry_list, node):
    # If no parent node, return -1
    valid_node = False
    for parent in ancestry_list:
            if parent[1] == node:
                valid_node = True
                break
    if valid_node == False:
        return -1

    # Use BFS to find earliest ancestor
    # Create an empty Queue to store paths to visited ancestors
    q = []
    # Enqueue with starting node
    q.append( [node] )
    visited = set()

    # While the queue is not empty...
    while len(q) > 0:
        # Dequeue the first path
        path = q.pop(0)
        # Grab the current node to search for ancestors
        curr_node = path[-1]
        # Find curr_node's ancestors
        if curr_node not in visited:
            visited.add(curr_node)
        
        no_parent = False

        for parent in ancestry_list:
            if parent[1] == curr_node:
                path_copy = list(path)
                path_copy.append(parent[0])
                q.append(path_copy)
                no_parent = True
        # If curr_node has no ancestors, break the loop
        if no_parent == False:
            q.append(list(path))
            break

    earliest = []
    for path in q:
        if len(path) > len(earliest):
            earliest = list(path)
        elif len(path) == len(earliest):
            if path[-1] < earliest[-1]:
                earliest = list(path)

    return earliest[-1]

print(earliest_ancestor(test_ancestors, 6))