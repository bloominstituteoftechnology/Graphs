"""
Simple graph implementation compatible with BokehGraph class.
"""

mygraph = {
    '0': {'1', '3'},
    '1': {'0'},
    '2': set(),
    '3': {'0'}
}

class Graph(object):
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
    def add_edge(self, target):
        # myg = nx.Graph(mygraph)
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
    def add_vertex(self, target):
        if target not in self.__graph_dict:
            self.__graph_dict[target] = []
