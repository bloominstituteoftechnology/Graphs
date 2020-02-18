from util import Queue
#     * The input will not be empty.
#     * There are no cycles in the input.
#     * There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
#     * IDs will always be positive integers.
#     * A parent may have any number of children.


def get_neighbors(a):
    '''
    return children's parents
    '''
    pass


def earliest_ancestor(ancestors, starting_node):
    '''
    use bfs to find the shortest path from child to ancestors
    '''
    q = Queue()
    # Enqueue path to starting word
    q.enqueue([starting_node])
    visited = set()
    # While queue is not empty...
    while q.size() > 0:
        # Dequeue path
        path = q.dequeue()
        # Grab ancestor from path
        a = path[-1]
        # Check if it's ancestors, if so return path
        if a == ancestors:
            return path
        # Check if it's been visited. If not...
        if a not in visited:
            # Mark it as visited
            visited.add(a)
            # Enqueue a path to each neighbor
            for neighbor in get_neighbors(a):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)
    return None
