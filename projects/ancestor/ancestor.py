def earliest_ancestor(ancestors, starting_node):
	ancestor, depth = spirit_medium(ancestors, starting_node)
	return ancestor if depth >= 0 else -1


def spirit_medium(ancestors, starting_node, parents=None):
    # need a place to store 
	if parents is None:
		parents = {}
		for parent, child in ancestors:
			if child not in parents:
				parents[child] = {parent}
			else:
				parents[child].add(parent)
		print(parents)
	# add a base case for when there are no parents
	if starting_node not in parents:
		return starting_node, -1

	deepest_node = None
	deepest_depth = 0
	for parent in parents[starting_node]:
		# no parents? we want to take the deepest
		if deepest_depth is 0:
			if deepest_node is None or parent < deepest_node:
				deepest_node = parent

		# keep going until we find the deepest ancestor
		node, depth = spirit_medium(ancestors, parent, parents=parents)
		if node is not None:
			if depth > deepest_depth:
				deepest_depth = depth
				deepest_node = node

			# If the ancestors are the same depth, get the deeper one
			elif depth == deepest_depth:
				if node < deepest_node:
					deepest_node = node

	return deepest_node, deepest_depth + 1