import collections

def earliest_ancestor(ancestors, starting_node):
    pass
    # So I need to build a graph from the input data, or at least a way to get the parents of each node
    # Let's loop through the ancestors and build a dictionary of parents to children, since we will be
    # traversing from the child up to the earliest ancestor

    # Then I need to find the path that is the longest, rather than the shortest
    # If I use breadth first traversal and return the LAST path in the queue, that should be the longest path

    parents_by_child = {}

    for parent, child in ancestors:
        if child in parents_by_child:
            parents_by_child[child].append(parent)
        else:
            parents_by_child[child] = [parent]

    # Early exit if the starting node has no parents
    if starting_node not in parents_by_child:
        return -1

    path_queue = collections.deque() # doubly ended queue

    last_path = [starting_node] # this will let us save the last path dequeued

    path_queue.append(last_path)

    while len(path_queue) > 0:
        last_path = path_queue.popleft()
        oldest_ancestor = last_path[-1]

        if oldest_ancestor in parents_by_child:
            parents_by_child[oldest_ancestor].sort(reverse=True) # make sure lowest id goes in queue last
            for parent in parents_by_child[oldest_ancestor]:
                new_path = last_path.copy()
                new_path.append(parent)

                path_queue.append(new_path)

    return last_path[-1]
