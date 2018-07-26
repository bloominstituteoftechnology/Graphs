#!/urs/bin/env python

"""
Demonstration of Graph and BokehGraph functionality
"""

from random import sample
from sys import argv
from draw import BokehGraph
from graph import Graph

def main(num_vertices=8, num_edges=8, test=False):
    """Build and show random graph."""
    graph = Graph()

    if test:     # Instantiate your graph
        graph.add_vertex('0')
        graph.add_vertex('1')
        graph.add_vertex('2')
        graph.add_vertex('3')
        graph.add_vertex('4')
        graph.add_vertex('5')
        graph.add_vertex('6')
        graph.add_vertex('7')
        graph.add_vertex('8')
        graph.add_vertex('9')
        graph.add_vertex('10')
    
        graph.add_edge('0', '1')
        graph.add_edge('0', '2')
        graph.add_edge('1', '3')
        graph.add_edge('1', '4')
        graph.add_edge('2', '5')
        graph.add_edge('2', '6')
        graph.add_edge('3', '1')
        graph.add_edge('4', '8')
        graph.add_edge('5', '9')
        graph.add_edge('9', '10')

        print(graph.search('10', 'bfs'))
        print(graph.vertices)

    else:
        # Add appropriate number of vertices
        for num in range(num_vertices):
            graph.add_vertex(str(num))

        # Add random edges between vertices
        for _ in range(num_edges):
            vertices = sample(graph.vertices.keys(), 2)
            # check if edge already exists
            graph.add_edge(vertices[0], vertices[1])

        print(graph.search('10'))
        print(graph.vertices)

    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show()


if __name__ == '__main__':
    if len(argv) == 3:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        main(NUM_VERTICES, NUM_EDGES)
    else:
        main()  # accept defaults