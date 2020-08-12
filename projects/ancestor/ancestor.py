# projects\ancestor\ancestors.py

import sys
sys.path.append(r"C:\Users\Samuel\repos\Graphs\projects\graph")

from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    """
    input
    ancestors, list of tuples with the first value reprensenting the parent
               and second value reprensenting the child.

    output,    obj (int) the 'top-most' parent in the family tree.
    """
    # Instantiate Graph object
    g = Graph()

    # Loop through tuples in ancestor list:
    for parent, child in ancestors:
        # Create vertices
        g.add_vertex(parent)
        g.add_vertex(child)

    for parent, child in ancestors:
        # Add edges
        # NOTE: the child is placed at the "top" of graph so that transverals
        #       flow to the ancestor rather than the other way around
        g.add_edge(child, parent)

    # if element has parents:
    if len(g.get_neighbors(starting_node)) > 0:
        # traverse list to earliest ancestors
        return g.bft_list(starting_node)[-1]

    else:
        return -1 


if __name__ == "__main__":
    ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

    print(earliest_ancestor(ancestors, 1))

