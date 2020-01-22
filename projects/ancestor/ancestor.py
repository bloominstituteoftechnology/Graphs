from util import Queue, Graph


def earliest_ancestor(ancestors, starting_node):
    # Create graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # Create reverse path edges
        graph.add_edge(pair[1], pair[0])
    # Establish placeholder for longest path
    max_path_len = 1
    # Establish place holder for oldest_ancestor
    earliest_ancestor = -1
    # Use BFS to store the path
    queue = Queue()
    queue.enqueue([starting_node])
    # While loop for existing nodes in queue
    while queue.size() > 0:
        # remove fist node
        path = queue.dequeue()
        # Get the last item in the current node
        vertex = path[-1]
        # If length of family is >= and the value is <, or if the length of family is longer
        if (len(path) >= max_path_len and vertex < earliest_ancestor) or (len(path) > max_path_len):
            # Updating earliest to curr_node
            earliest_ancestor = vertex
            # Updating curr_size
            max_path_len = len(path)
            # Traversing parents
        for neighbor in graph.vertices[vertex]:
            # Make family copy
            path_copy = list(path)
            # Append curr_node to copy of family
            path_copy.append(neighbor)
            # Enqueue to family copy
            queue.enqueue(path_copy)

    return earliest_ancestor




