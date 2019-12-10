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
    graph = Graph()
    
    # Add the nodes
    for i in ancestors:
        graph.add_vertex(i[1])
        graph.add_vertex(i[0])
        #print("node: ", i[1])
    #print("Nodes only: ")
    #print(graph.vertices)
    for i in ancestors:
        graph.add_edge(i[1], i[0])
        #print("tuple: ", i)
        #print("neighbor: ", i[0])
    #print("Nodes + neighbors: ")
    print(graph.vertices)

    
