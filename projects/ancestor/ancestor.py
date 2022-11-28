

#  test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
#         self.assertEqual(earliest_ancestor(test_ancestors, 1), 10)


def earliest_ancestor(ancestors, starting_node):
    # Create an ancestor tree
    ancestor_tree = {}
    # Loop through the list 
    for relationship in ancestors:
        # If the child is not in the tree
        if relationship[1] not in ancestor_tree:
            # Assign the parent to the child as an array of parents
            ancestor_tree[relationship[1]] = [relationship[0]]
        else:
            # Otherwise just add the value
            ancestor_tree[relationship[1]].append([relationship[0]])
    # Use a DFT to get to the last parent
    def recursion(graph, vertex):
        # If the vertex is not in the graph
        if vertex not in graph:
            # Return a generation counter plus the vertex
            return(1, vertex)
        # Create storage for results
        results = []
        # Recursively call through the graph
        for value in graph[vertex]:
            results.append(recursion(graph, value))
        # If there is only one ancestor
        if len(results) == 1:
            # Increment the generation and return the ancestor
            return(results[0][0] + 1, results[0][1])
        
        # If there are more than one ancestors, check which is greater
        if results[0][0] > results[0][1]:
            # Increment the generation and return the ancestor
            return(results[0][0] + 1, results[0][1])
        elif results[0][0] < results[0][1]:
            # Increment the generation and return the ancestor
            return(results[1][0] + 1, results[1][1])
        else:
            # If the generation is the same, return the smaller value
            if results[0][1] < results[1][1]:
                # Increment the generation and return the ancestor
                return(results[0][0] + 1, results[0][1])
            else:
                # Increment the generation and return the ancestor
                return(results[1][0] + 1, results[1][1])
    #  Grab the earlist ancestor
    return_ancestor = recursion(ancestor_tree, starting_node)
    # Check if there are ancestors (check against the incremented value)
    if return_ancestor[0] == 1:
        # If no ancestors return -1
        return -1
    else:
        # Otherwise return the ancestor
        return return_ancestor[1]