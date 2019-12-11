from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # 1) Build ancestors data into a set or whatever its called
    # 2) Traverse from starting node to find longest string/path
    # 3) There is no path or destionation - just traverse the entire 
    # thing and find the longest possible string

    """
    Add nodes
    Add edges
    """
    g = Graph()
    
    # Add the nodes
    # for i in ancestors:
    #     graph.add_vertex(i[1])
    #     graph.add_vertex(i[0])
    # for i in ancestors:
    #     graph.add_edge(i[1], i[0])
    # print("Nodes + neighbors: ")
    # print(graph.vertices)
    # print("DFT solution")
    # print(graph.dft_recursive(6))
    # print("end of solution")

    # def earliest_ancestor(ancestors, starting_node):
    # path = []
    
    ####  ---- Works------  ####

    # Building the Graph
    for e in ancestors:
        g.add_edge(e[1], e[0])        
    
    # Get set of visted nodes from Traversal

    # Visited = returns each and every node that's possible from starting node
    visited = g.dft(starting_node)
    # Doesn't work right now - need to pass it an array/dictionary that can receive nodes
    # So for-loop below has something to iterate over
    # d.dft doesn't return anything as-written

    # Doing a search from starting_node to each vertices that is traversed to get longest path
    # Run a search on each node returned from visited, 
    # check its path length

    for v in visited:
        path_to_each = g.dfs(starting_node, v)
        if len(path_to_each) > len(path):
            path = path_to_each
        if len(path_to_each) == len(path) and path_to_each[-1] < path[-1]:
            path = path_to_each
    if len(path) == 1:
        return -1
    
    return path[-1]


    
