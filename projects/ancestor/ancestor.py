from util import Graph, Queue

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    terminal_paths = []
    
    # Add nodes and edges to graph
    for pair in ancestors:
        for v in pair:
            # Add nodes if not already in g.vertices
            if v not in g.vertices:
                g.add_vertex(v)
        # Add unidirectional edge representing the "is a child of" relation
        g.add_edge(pair[1], pair[0])

    # Create an empty queue
    q = Queue()
    # Add a path from the starting node to the queue
    q.enqueue( [starting_node] )
    # Create an empty set
    visited = set()
    # While the queue is not empty
    while q.size() > 0:
        # Dequeue the first path
        path = q.dequeue()
        # Grab the last vertex from the path
        v = path[-1]
        # Check if it has parents
        if g.get_neighbors(v)==set():
            # If not, append to list of terminal paths
            terminal_paths.append(path)
        # Check if node has been visited
        if v not in visited:
            # If not, mark it visited
            visited.add(v)
            # For each parent
            for neighbor in g.get_neighbors(v):
                # Make a copy of the path before adding
                path_copy = path.copy()
                # Add the parent to the path
                path_copy.append(neighbor)
                # Add the appended path to the queue
                q.enqueue(path_copy)
    
    # Find how long the longest path is in terminal_paths
    max_length = max(len(p) for p in terminal_paths)
    # Create a list of all paths that are of length max_length
    longest_paths = [p for p in terminal_paths if len(p)==max_length]

    # Return -1 if the starting node has no parents
    if max_length == 1:
        return -1
    # If there's a unique longest path, return the earliest ancestor from the end of it
    if len(longest_paths)==1:
        return longest_paths[0][-1]
    # If there are multiple longest paths, return the earliest ancestor with the lowest id number
    if len(longest_paths)>1:
        candidates = [p[-1] for p in longest_paths]
        return min(candidates)
    