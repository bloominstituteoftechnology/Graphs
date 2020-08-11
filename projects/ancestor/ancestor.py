# projects\ancestor\ancestors.py

import sys
sys.path.append(r"C:\Users\Samuel\repos\Graphs\projects\graph")

from graph import Graph

def earliest_ancestor(ancestors, starting_node=None):
    """
    input
    ancestors, list of tuples with the first value reprensenting the parent
               and second value reprensenting the child

    output, obj (int) the 'top-most' parent in the family tree.
    """
    # Instantiate Graph object
    g = Graph()

    # Loop through tuples in ancestor list:

    # This makes the graph, upside-down
    # for each parent, child in ancestors:
        # graph.add_vertex(child)
        # graph.add_edge(parent)

    for parent, child in ancestors:
        g.add_vertex(parent)
        g.add_edge(child)
    
    # Use breadth-first approach,
    # labeling each layer with a counter
    # corrosponding to the generation to which it belongs

    return 


if __name__ == "__main__":
    ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

    earliest_ancestor(ancestors)

