def earliest_ancestor(ancestors, starting_node):
    graph = {}

    # Build graph of children's parents
    for (parent, child) in ancestors:
        if child in graph:
            graph[child].add(parent)
        else:
            graph[child] = {parent}

    next_verts = [(0, starting_node)]
    visited = set()
    oldest = next_verts[0]
    while len(next_verts) > 0: 
        depth, current = next_verts.pop()

        if current in visited:
            continue
        visited.add(current)

        if depth > oldest[0] or depth == oldest[0] and current < oldest[1]:
            oldest = (depth, current)

        if current not in graph:
            continue

        for parent in graph[current]:
            next_verts.append((depth + 1, parent))

    if oldest[1] == starting_node:
        return -1
    return oldest[1]

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 1)) # 10
print(earliest_ancestor(test_ancestors, 2)) # -1
earliest_ancestor(test_ancestors, 3) # 10
earliest_ancestor(test_ancestors, 4) # -1
earliest_ancestor(test_ancestors, 5) # 4
earliest_ancestor(test_ancestors, 6) # 10
earliest_ancestor(test_ancestors, 7) # 4
earliest_ancestor(test_ancestors, 8) # 4
earliest_ancestor(test_ancestors, 9) # 4
earliest_ancestor(test_ancestors, 10) # -1
earliest_ancestor(test_ancestors, 11) # -1