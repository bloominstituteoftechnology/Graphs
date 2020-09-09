

#  test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
#         self.assertEqual(earliest_ancestor(test_ancestors, 1), 10)


def earliest_ancestor(ancestors, starting_node):

    # Create an ancestor tree
    ancestor_tree = {}

    # Loop through the list 
    for relationship in ancestors:
        # If the child is not in the tree
        if relationship[1] not in ancestor_tree:
            # Assign the parent to the child
            ancestor_tree[relationship[1]] = [relationship[0]]
        else:
            # Otherwise just add the value
            ancestor_tree[relationship[1]].append([relationship[0]])
    # Use a DFT to get to the last parent
    def recursion(graph, vertex):
        # If the vertex is not in the graph
        if vertex not in graph:
            # Return a counter plus the vertex
            return(1, vertex)
        # Create storage for results
        results = []

        # Recursively call through the graph
        for value in graph[vertex]:
            results.append(recursion(graph, value))

        # If there is only one ancestor
        if len(results) == 1:
            return(results[0][0] + 1, results[0][1])
        
        # If there are more than one ancestors
        if results[0][0] > results[0][1]:
            return(results[0][0] + 1, results[0][1])
        elif results[0][0] < results[0][1]:
            return(results[1][0] + 1, results[1][1])
        else:
            # If the generation is the same, return the smaller value
            if results[0][1] < results[1][1]:
                return(results[0][0] + 1, results[0][1])
            else:
                return(results[1][0] + 1, results[1][1])
    #  Grab the earlist ancestor
    return_ancestor = recursion(ancestor_tree, starting_node)
    if return_ancestor[0] == 1:
        return -1
    else:
        return return_ancestor[1]


    # earliest_ancestor = None
    # # Build the tree
    # for relationship in ancestors:
    #     # Check if the parent value is in the tree
    #     if relationship[0] not in ancestor_tree:
    #         # If not, add it
    #         ancestor_tree[0]["child"] = [ancestor_tree[1]]
    #     # If the parent value is in the tree
    #     if relationship[0] in ancestor_tree:
    #         # Get the current list of children
    #         original_child_list = ancestor_tree.get("child")
    #         #Create a new list
    #         new_list = []
    #         #  Loop through the original list
    #         for item in original_child_list:
    #             # Append all items to the new list
    #             new_list.append(item)
    #         # Append the the current child to the new list
    #         new_list.append(relationship[1])
    #         # Assign the new list to the 'child' key for the parent value
    #         ancestor_tree[0]["child"] = new_list
    #     # If the child is already in the tree
    #     if relationship[1] in ancestor_tree:
    #         # Assign the current parent value as the parent of the child already present in the tree.
    #         ancestor_tree[1]["parent"] = [ancestor_tree[0]]

    # # Check if the starting node is a key in the ancestor_tree
    # if starting_node in ancestor_tree:
    #     # Grab the current node
    #     node = ancestor_tree[starting_node]
    #     # If the node has parents
    #     if node["parents"]:
    #         # Check only one parent
    #         if len(node["parents"]) == 1:
    #             # Return the single parent
    #             return node["parents"]
    #         else:
    #             # Check if the first parent value is greater than the second parent value
    #             if node["parents"][0] > node["parents"][1]:
    #                 return node["parents"][0]
    #             else:
    #                 return node["parents"][1]
    # return earliest_ancestor

    # returns their earliest known ancestor 
    # – the one at the farthest distance from the input individual. 
    # If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. 
    # If the input individual has no parents, the function should return -1.