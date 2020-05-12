from graph import Graph


def earliest_ancestor(ancestors, starting_node):
	"""
	Create graph
	Add verticies
	Add edges
	"""
	tree = Graph()                          # Create the graph
	for (node_1, node_2) in ancestors:      # For each node in ancestors (check testing)
		tree.add_vertex(node_1)             # Add vertex for x (x, y)
		tree.add_vertex(node_2)             # Add vertex for y (x, y)

	for (node_1, node_2) in ancestors:      # For each node in ancestors (check testing)
		tree.add_edge(node_1, node_2)       # Add an edge between the two nodes (x, y)

	target_node = None                      # We have no target node yet, so default is None
	longest_path = 1                        # Default longest path to 1; 0 errors; We will move at least once

	for node in tree.vertices:                  # There are neighbor nodes for each vertex
		path = tree.dfs(node, starting_node)    # Run a DFS starting at current node to starting node
												# This will tell us how far current node is from start
		if path:                                # If path exists
			if len(path) > longest_path:        # If length of path (int) is longer than longest_path(also int)
				longest_path = len(path)        # Updated longest_path (int) to length of path (int)
				target_node = node              # Target node becomes current node
		elif not path and longest_path == 1:    # If path returns none and lp is 1
			target_node = -1                    # Set TN to -1; No idea why; Look at testing
	return target_node                          # After all of this, return the target node

"""
Target node is set to none because we don't actually know what we're looking for... yet

Path is the result of the DFS where we are seeing how far away 
the each node is from the starting node

If path returns something
And the length of the path is greater than the current longest path
Set the target_node to the node we are on

If path doesn't return anything AND the longest_path is 1
Set target node it -1; No idea why, but that's what the test calls for

At the end, return the target node

The loop will run over every node, only updating the longest_path/target_node when the 
current node is further away from the previous node

The loop will automatically break when path doesn't return anything
"""
