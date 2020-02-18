from util import Stack, Graph

ancestors_data = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):
    ancestor_tree = Graph()
    # Iterate through ancestors
    for (parent, child) in ancestors:  
        # Add vertices to ancestor_tree
        ancestor_tree.add_vertex(parent)
        ancestor_tree.add_vertex(child)
    # print("ancestor tree", ancestor_tree.vertices)
    
    for (parent, child) in ancestors:
        # Add edges
        ancestor_tree.add_edge(child, parent)
    # print("neighbors", ancestor_tree.get_neighbors(5))
    # print("ancestor tree", ancestor_tree.vertices)

    longest_path = 1  # Keep track of # ancestors; highest means most ancestors
    earliest_ancestor = 0 # Store last node (as an integer)
    for i in ancestor_tree.vertices:
        # print("i", i)  # Print vertices
        # Call dfs function from Graph class
        path = ancestor_tree.dfs(i, starting_node)  # i is each vertex/node in graph
        # print("ancestor dfs", ancestor_tree.dfs(starting_node, i))
        print('path', path)
        if path:  # If there are items in list
            if len(path) > longest_path:  # If list length is greater than longest path
                longest_path = len(path)  # Set longest path equal to list length
                earliest_ancestor = i  # Set earliest_ancestor equal to current node/vertex
        elif not path and longest_path == 1:  # If path is 'None' and 'longest_path' is our default of 1   
            earliest_ancestor = -1
                
    print("earliest ancestor", earliest_ancestor)
    return earliest_ancestor

print('earliest ancestor', earliest_ancestor(ancestors_data, 8))

'''
BFS Solution:
def earliest_ancestor(ancestors, starting_node):
    # Build graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # Build edges in reverse
        graph.add_edge(pair[1], pair[0])
    
    # Do a BFT (storing the path)
    q = Queue()
    q.enqueue([starting_node])
    max_path_len = 1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        # If the path is longer or equal and the value is smaller, or if the path is longer
        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)

        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)

    return earliest_ancestor

'''