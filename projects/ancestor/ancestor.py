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
        ancestor_tree.add_edge(parent, child)
    # print("neighbors", ancestor_tree.get_neighbors(5))
    # print("ancestor tree", ancestor_tree.vertices)

    longest_path = 1  # Keep track of # ancestors; highest means most ancestors
    earliest_ancestor = 0 # Store last node (as an integer)
    for i in ancestor_tree.vertices:
        # print("i", i)  # Print vertices
        # Call dfs function from Graph class
        dfs_list = ancestor_tree.dfs(i, starting_node)  # i is each vertex/node in graph
        # print("ancestor dfs", ancestor_tree.dfs(starting_node, i))
        if dfs_list:  # If there are items in list
            if len(dfs_list) > longest_path:  # If list length is greater than longest path
                longest_path = len(dfs_list)  # Set longest path equal to list length
                earliest_ancestor = i  # Set earliest_ancestor equal to current node/vertex
        
    print("earliest ancestor", earliest_ancestor)
    return earliest_ancestor

# print('earliest ancestor', earliest_ancestor(ancestors_data, 8))