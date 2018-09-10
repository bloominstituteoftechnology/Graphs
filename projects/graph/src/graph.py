"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        pass  # TODO




#need a way to store edges and store vertices values

#one way is through objects and pointers (should be familiar with this because we've worked with linked lists)
    # * each node is a pointer to an object and each edge is a pointer (like a linked list, each element POINTS to the next element in the linked list). "You're storing a list of pointers (pointers another way of saying edges, i guess.)"





#### Graph implementation must be compatible with BokehGraph (see: https://bokeh.pydata.org/en/latest/docs/user_guide/graph.html)
# -The ColumnDataSource associated with the node sub-renderer must have 
# a column named "index" that contains the unique indices of the nodes.
# -The ColumnDataSource associated with the edge sub-renderer has two 
# required columns: "start" and "end". These columns contain the node
# indices of for the start and end of the edges.