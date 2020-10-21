
def earliest_ancestor(ancestors, starting_node):
    # Create adjacency_list list from ancestors
    adjacency_list = {}
    for ancestor_pair in ancestors:
        if ancestor_pair[0] not in adjacency_list:
            adjacency_list[ancestor_pair[0]] = set()
        if ancestor_pair[1] not in adjacency_list:
            adjacency_list[ancestor_pair[1]] = set()
        adjacency_list[ancestor_pair[1]].add(ancestor_pair[0])

    print(adjacency_list)    
    # Create a queue with starting_node
    queue = [ [starting_node] ]
    # Create a visited set to track the vertices
    visited = set()
    # While queue is not empty
    max_path_length = 1
    current_earliest_ancestor = -1
    while len(queue)>0:
        # Dequeue the current_path with vertex from the queue 
        current_path = queue.pop(0)
        # Get the current_vertex from the current_path
        current_vertex = current_path[-1]
        print(f'Now exploring vertex {current_vertex} from start vertex {starting_node}')
        print(current_path)
        # If current_vertex is not in visited
        if current_vertex not in visited:
            # Add the vertex to the visited
            visited.add(current_vertex)
            if (len(current_path) > max_path_length or len(current_path) >= max_path_length) and current_vertex < current_earliest_ancestor:
                max_path_length = len(current_path)
                current_earliest_ancestor = current_vertex
            # Explore the neighbors of the current_vertex - add it to queue
            for neighbor in adjacency_list[current_vertex]:
                # copy the current path
                new_path = list(current_path)
                # add the neighbor to it
                new_path.append(neighbor)
                queue.append(new_path)

    return current_earliest_ancestor
     