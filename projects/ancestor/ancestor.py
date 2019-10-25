class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node] = set()

    def add_edge(self, v1, v2):
        if v1 not in self.nodes:
            self.add_node(v1)
        if v2 not in self.nodes:
            self.add_node(v2)
        self.nodes[v2].add(v1)

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

# breath first treversal
# returns array of all paths related to given node
def bft_find_all_paths(graph, starting_node):
	queue = Queue()
	queue.enqueue([starting_node])
	visited = set() # all visited nodes
	all_paths = []

	while queue.size() > 0:
		path = queue.dequeue()
		node = path[-1]

		if node not in visited:
			visited.add(node)
			if len(graph.nodes[node]) > 0:
				all_paths = []
			for new_node in graph.nodes[node]:
				new_path = list(path)
				new_path.append(new_node)
				if len(graph.nodes[new_node]) == 0:
					all_paths.append(new_path)
				else:
					queue.enqueue(new_path)

	return all_paths

def earliest_ancestor(ancestors, starting_node):
	graph = Graph()

	# populates graph
	for ancestor in ancestors:
		graph.add_edge(ancestor[0], ancestor[1])


	all_paths = bft_find_all_paths(graph, starting_node)

	# assigns -1 if no paths exist otherwise assigns last value of first path 
	answer = -1 if len(all_paths) == 0 else all_paths[0][-1]

	if len(all_paths) > 1:
		for i in range(len(all_paths)-1):
			if all_paths[i+1][-1] < answer:
				answer = all_paths[i+1][-1]

	return answer