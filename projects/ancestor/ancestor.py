
def earliest_ancestor(ancestors, starting_node):
    parent_child_dict = {}
    for relationship in ancestors:
        parent = relationship[0]
        child = relationship[1]
        if child not in parent_child_dict:
            parent_child_dict[child] = set()
        parent_child_dict[child].add(parent)

    earliest_ancestor = -1

    queue = []
    queue.append(starting_node)
    while len(queue) > 0:
        curr_vertex = queue.pop()
        if curr_vertex in parent_child_dict:
            parent_with_lowest_ID = None
            for parent in parent_child_dict[curr_vertex]:
                if parent_with_lowest_ID is None:
                    parent_with_lowest_ID = parent
                elif parent < parent_with_lowest_ID:
                    parent_with_lowest_ID = parent
                queue.append(parent)
            if parent_with_lowest_ID is not None:
                earliest_ancestor = parent_with_lowest_ID

    return earliest_ancestor
