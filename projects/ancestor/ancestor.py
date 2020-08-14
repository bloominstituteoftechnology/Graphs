from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # Create a graph
    # Create target node variable
    # Create longest path variable
    graph = Graph()

    # Add Vertices to Graph
    for (vertex1, vertex2) in ancestors:
        graph.add_vertex(vertex1)
        graph.add_vertex(vertex2)

    for (vertex1, vertex2) in ancestors:
        graph.add_edge(vertex1, vertex2) # Add edges to Vertices since looping already

    target = -1
    longest_path = 1

#     print(graph.vertices)
#     path = graph.dft(starting_node)
#     print(path)

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(test_ancestors, 1))

    # if len(path) > longest_path:
    #     longest_path = len(path)
    #     target = path

    # Loop through the vertices in the graph.
    for vertices in graph.vertices:

        # Path is set to the graphs DFS method
        path = graph.dfs(vertices, starting_node)

        # If Path is not None:
        if path:

            # If the length of path is greater than the longest path var
            if len(path) > longest_path:

                # The longest path = len(path)
                longest_path = len(path)

                # Target node var is set equal to that node
                target = vertices

            # Else
            elif not path and longest_path == 1:
                target = -1
            
            else:
                target = -1

    # At long last return the target node because that's what we want
    return target

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 8))

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

def earliest_ancestor_solve(ancestors, starting_node):
    # Build the graph
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])

    # Do a BFS storing the path (Either BFS or DFS will work)
    queue = Queue()
    queue.enqueue([starting_node])
    max_path_length = 1
    earliest_ancestor = -1
    while queue.size() > 0:
        path = queue.dequeue()
        last_vertex = path[-1]
        if (len(path) >= max_path_length and last_vertex < earliest_ancestor) or (len(path) > max_path_length):
            earliest_ancestor = last_vertex
            max_path_length = len(path)
            for neighbor in graph.vertices[last_vertex]:
                path_copy = list(path)
                path_copy.append(neighbor)
                queue.enqueue(path_copy)
    return earliest_ancestor

print(earliest_ancestor_solve(test_ancestors, 8))