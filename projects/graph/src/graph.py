#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

from random import randint

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.graph = {}
        self.graph_list = []

    def add_vertex(self, vertice):
        self.graph[ vertice ] = set()

    def add_edge(self, node, connect_node):
        self.graph[ node ].add(connect_node)

    def breadth_first_search(self, node_value):
        # if node_value not in self.graph:
        #     print(f"Graph.breadth_first_search() expects a single value passed as an argument")
        #     return None
        
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

    def add_random_vertices(self, max_vertice):
        for _ in range(randint(2, int(max_vertice))):
            rand = randint(0, int(max_vertice))

            if rand not in self.graph:
                self.add_vertex(rand)
                self.graph_list.append(rand)

    def add_random_edges(self):
        done = False
        i = 0
        j = 0

        while not done:
            if j >= len(self.graph_list):
                j = 0
                i += 1

            if i >= len(self.graph_list):
                break
            
            current = self.graph_list[ i ]

            if current == self.graph_list[ j ]:
                j += 1
                continue

            if self.graph_list[ j ] not in self.graph[ current ]:
                if randint(0, 1) == True:
                    self.graph[ current ].add(self.graph_list[ j ])

            j += 1

# graph = Graph()

# graph.add_random_vertices(9)
# graph.add_random_edges()

# print(graph.graph, '\n')

# graph.add_vertex(rand_int)
# graph.add_vertex(rand_int)
# graph.add_vertex(rand_int)

# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# graph.add_edge('1', '2')
# graph.add_edge('2', '3')
# graph.add_edge('3', '1')

# graph.breadth_first_search(1) # {'0': {'1', '3'}, '1': {'2'}, '2': {'3'}, '3': {'1'}}