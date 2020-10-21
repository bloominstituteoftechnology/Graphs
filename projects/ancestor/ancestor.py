
def earliest_ancestor(ancestors, starting_node):
    
    # Create a queue with starting_node
    queue = [ [starting_node] ]
    # Create a visited set to track the vertices
    visited = set()
    # While queue is not empty
    while len(queue)>0:
        # Dequeue the current_path with vertex from the queue 
        current_path = queue.pop(0)
        # Get the current_vertex from the current_path
        current_vertex = current_path[-1]
        # If current_vertex is not in visited
        if current_vertex not in visited:
            # Add the vertex to the visited
            visited.add(current_vertex)
            # Explore the neighbors of the current_vertex - add it to queue
            for neighbor in adjacency_list[current_vertex]:
                # Get the copy of the current_path
                current_path.copy = list(current_path)
                # Add neighbor to the current_path
                current_path.copy.append(neighbor)
                # Add the whole current path copy to the queue
                queue.append(current_path.copy)

