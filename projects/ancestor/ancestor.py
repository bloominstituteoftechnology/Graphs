import sys
sys.path.append("../graph")
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    parent = 0
    child = 1
    
    graph = Graph()
    #add vertex
    for ancestor in ancestors: 
        graph.add_vertex(ancestor[child])
        graph.add_vertex(ancestor[parent])

    #add edge
    for ancestor in ancestors:
        graph.add_edge(ancestor[child],ancestor[parent])
        
    return graph.bft_find_furthest(starting_vertex=starting_node)