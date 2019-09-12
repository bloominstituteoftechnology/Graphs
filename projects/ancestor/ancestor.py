class Stack:
	def __init__(self):
		self.stack = []
	def push(self, value):
		self.stack.append(value)
	def size(self):
		return len(self.stack)
	def pop(self):
		if self.size() > 0:
			return self.stack.pop(-1)
		else:
			return 0

def earliest_ancestor(ancestors, starting_node):
	# Depth first search (stack)

	stack = Stack()
	stack.push([starting_node])
	# visited = set()

	longest_path = [starting_node]
	e_ancestor = starting_node
	has_parent = False

	while stack.size() > 0:

		path = stack.pop()

		if (len(path) > len(longest_path)) or (path[0] < longest_path[0]):
			longest_path = path.copy()
			# print(path)
			e_ancestor = path[0]

		top_value = path[0]

		for t in ancestors:
			if t[-1] == top_value:
				path_copy = path.copy()
				path_copy.insert(0, t[0])
				stack.push(path_copy)
				has_parent = True

		if has_parent == False:
			e_ancestor = -1

	return e_ancestor