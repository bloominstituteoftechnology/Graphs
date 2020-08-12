def earliest_ancestor(ancestors, starting_node):
	
	# Map graph
	graph = {}
	for parent, child in ancestors:
		if child not in graph:
			graph[child] = {parent}
		else:
			graph[child].add(parent)

	stack = []
	stack.append([starting_node]) # Starting Node

	visited = set()
	longestPath = []

	while len(stack) > 0:
		path = stack.pop() # Last in First out
		vert = path[-1]

		# Current path is same length as longest but parent has smaller value,
		# or path longer than existing longest
		if (len(path) == len(longestPath) and path[-1] < longestPath[-1] or len(path) > len(longestPath)):
			longestPath = path

		if vert in graph: # vert has parent
			for parent in graph[vert]:
				newPath = list(path)
				newPath.append(parent)
				stack.append(newPath)

	if longestPath[-1] == starting_node:
		return -1
	else:
		return longestPath[-1]





if __name__ == '__main__':
	ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

	for i in range(1,12):
		print(i, ":", earliest_ancestor(ancestors, i), "\n")
		