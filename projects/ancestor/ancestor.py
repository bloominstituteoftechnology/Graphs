
def earliest_ancestor(ancestors, starting_node):
	ancestor, depth = earliest_ancestor_internal(ancestors, starting_node)
	return ancestor if depth >= 0 else -1


def earliest_ancestor_internal(ancestors, starting_node, parents=None):
	if parents is None:
		parents = {}
		for parent, child in ancestors:
			if child not in parents:
				parents[child] = {parent}
			else:
				parents[child].add(parent)

	# Base case: No parents
	if starting_node not in parents:
		return starting_node, -1

	deepest_node = None
	deepest_depth = 0
	for parent in parents[starting_node]:
		# If the parents don't have parents, we want to default to the one with the lowest val
		if deepest_depth is 0:
			if deepest_node is None or parent < deepest_node:
				deepest_node = parent

		# Recurse to find the parents' deepest ancestors
		node, depth = earliest_ancestor_internal(ancestors, parent, parents=parents)
		if node is not None:
			if depth > deepest_depth:
				deepest_depth = depth
				deepest_node = node

			# If the ancestors are the same depth, get the one with the lower val
			# There are several ways to do this, but explicit is more legible
			elif depth == deepest_depth:
				if node < deepest_node:
					deepest_node = node

	return deepest_node, deepest_depth + 1
