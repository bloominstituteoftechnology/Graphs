"""
Demonstration of Graph and BokehGraph functionality.
"""

from random import sample
from sys import argv
from draw import BokehGraph
from graph import Graph, Vertex


def main():
    """Build and show random graph."""
    """graph = Graph()
    # Add appropriate number of vertices
    for num in range(num_vertices):
        graph.add_vertex(str(num))

    # Add random edges between vertices
    for _ in range(num_edges):
        vertices = sample(graph.vertices.keys(), 2)
        # TODO check if edge already exists
        graph.add_edge(vertices[0], vertices[1])
    """
    graph = Graph()

    graph.create_vertices_and_edges(10)
    graph.get_connected_components()
    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show()


if __name__ == '__main__':
    main()

    """if len(argv) == 3:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        main(NUM_VERTICES, NUM_EDGES)
    else:"""

"""from graph import Graph
from draw import BokehGraph


def main():
    print("hello")
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_vertex('F')
    graph.add_vertex('G')
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('E', 'F')
    graph.add_edge('F', 'G')
    bg = BokehGraph(graph)
    bg.plot
    bg.show()

if __name__ == '__main__':
    main()
"""
