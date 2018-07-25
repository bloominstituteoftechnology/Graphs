#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertice):
        self.graph[ vertice ] = set()

    def add_edge(self, node, connect_node):
        self.graph[ node ].add(connect_node)

    def breadth_first_search(self, node_value):
        if node_value not in self.graph:
            print(f"Graph.breadth_first_search() expects a single value passed as an argument")
            return None
        
        queue = []
        queue_set = set()
        queue.append(node_value)
        queue_set.add(node_value)
        
        i = 0

        while i < len(queue):
            current = self.graph[ queue[ i ] ]

            for edge in current:
                if edge not in queue_set:
                    queue.append(edge)
                    queue_set.add(edge)

            i += 1

graph = Graph()

graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')

graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('1', '2')
graph.add_edge('2', '3')
graph.add_edge('3', '1')

graph.breadth_first_search(1) # {'0': {'1', '3'}, '1': {'2'}, '2': {'3'}, '3': {'1'}}