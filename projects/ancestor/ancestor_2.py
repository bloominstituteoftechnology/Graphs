class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
    
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)



def earliest_ancestor(ancestors, starting_node):
    ## using the graph class
    graph = Graph()

    ## build a dictionary of all the connections
    for connection in ancestors:
        graph.add_vertex(connection[1])

    for connection in ancestors:
        graph.add_edge(connection[1], connection[0])

    ## empty set to store the paths (set of lists)
    paths = []
    visited_paths = []

    visited_paths.append([starting_node])

    while len(visited_paths) > 0:
        current_path = visited_paths.pop(0)
        starting_node = current_path[-1]

        if starting_node in graph.vertices:
            for parent in graph.vertices[starting_node]:
                new_path = current_path.copy()
                new_path.append(parent)
                paths.append(new_path)
                visited_paths.append(new_path)

    if len(paths) == 0:
        return -1    
    longest = max([len(i) for i in paths])
    plist = []
    for path in paths:
        if len(path) == longest:
            plist.append(path)
    
    oldest = []
    for path in plist:
        oldest.append(path[-1])
    
    return min(oldest)    


if __name__ == '__main__':
    unittest.main()




