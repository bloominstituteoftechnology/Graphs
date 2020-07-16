from projects.graph.graph import Graph
def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors:
        a = pair[0]
        b = pair[1]
        graph.add_edge(pair[0], pair[1])
    print(graph.vertices)
