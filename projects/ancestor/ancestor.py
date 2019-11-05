from graph import Graph
from util import Queue


def bfs(graph, starting_vertex):
    """
    Return a list containing the longest path 
    from starting_vertex  
    """
    earliest_an = None
    # Create an empty queue and enqueue A PATH TO the starting vertex ID
    q = Queue()
    initial_path = [starting_vertex]
    q.enqueue(initial_path)
    # Create a Set to store visited vertices
    visited = set()
    # While the queue is not empty...
    while q.size() > 0:
        # Dequeue the first PATH
        path = q.dequeue()
        # save the length of the path
        path_length = len(path)
        # Grab the last vertex from the PATH
        last_vert = path[-1]
        # If that vertex has not been visited...
        if last_vert not in visited:
            # Mark it as visited...
            visited.add(last_vert)
            # Then add A PATH TO its neighbors to the back of the 
            for v in graph.vertices[last_vert]:
                # COPY THE PATH
                path_copy = path[:]
                # APPEND THE NEIGHOR TO THE BACK
                path_copy.append(v)
                q.enqueue(path_copy)
                # If the new path is longer than previous path 
                # Save the longer path as earliest_ancestor
                if len(path_copy) > path_length:
                    earliest_an = path_copy
    if earliest_an:
        return earliest_an[-1]
    return -1
        


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for a in ancestors:
        # Add all vertices to graph
        graph.add_vertex(a[0])
        graph.add_vertex(a[1])
    for a in ancestors:
        # Create child to parent relationship 
        graph.add_edge(a[1], a[0])
    return bfs(graph, starting_node)



test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 1))