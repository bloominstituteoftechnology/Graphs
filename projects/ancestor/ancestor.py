class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        # Create the vertice if needed.
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)

        # Now add the edge from v1 to v2
        self.vertices[v1].add(v2)

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):
    # Walking through the after hours video and code.
    # We create a new Graph to handle the set pairs being passed into the function.
    graph = Graph()

    # We need to add the vertices and edges between them...
    for group in ancestors:
        l = list(group) # Convert it to a list
        graph.add_edge(l[1], l[0]) # Pass the second and first element in

    queue = [] # It's a breadth first search
    bft_path = [] 
    highest_nodes = []
    visited = set() #  Hey! I recognize this. =]

    queue.append(starting_node)
    highest_nodes.append(starting_node)
    visited.add(starting_node)
    index = len(highest_nodes)
    count = len(highest_nodes)

    while True:
        node = queue.pop(0)
        bft_path.append(node) # add the current node to the breadth first path

        # Add the current node's parents to highest nodes...
        highest_nodes += list(graph.vertices[node])
        print(highest_nodes)
        # Break out of the loop if the queue is empty and we're out of parents
        if not len(queue) and not graph.vertices[node]:
            break

        count -= 1

        if not count:
            highest_nodes = highest_nodes[index:]
            count = len(highest_nodes)
            index = len(highest_nodes)

        for parent in graph.vertices[node]:
            if parent not in visited:
                queue.append(parent)
                visited.add(parent)
        
        if highest_nodes[0] == starting_node:
            return -1
        else:
            return min(highest_nodes)

earliest_ancestor(test_ancestors, 1)