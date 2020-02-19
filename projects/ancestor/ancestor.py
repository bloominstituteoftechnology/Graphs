from graph import Graph

def earliest_ancestor(ancestors, starting_node):

    # initialize graph
    g = Graph()
    g.add_vertex(starting_node)

    # add ancestors to graph
    for pair in ancestors:
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])
    
    # add edge
    for pair in ancestors:
        # edge created from child to parent
        g.add_edge(pair[1], pair[0])
    
    test = g.ancestor_search(starting_node)[0]

    if test == starting_node:
        return -1
    else:
        return test

#  1 3
#   2 3
#   3 6
#   5 6
#   5 7
#   4 5
#   4 8
#   8 9
#   11 8
#   10 1