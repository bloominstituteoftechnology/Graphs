from draw import BokehGraph
from graph import Graph
from graph import Vertex
from sys import argv


def main():
    graph = Graph()
    v1 = Vertex("A")
    v2 = Vertex("B")

    graph.add_vertex(v1)
    graph.add_vertex(v2)
    graph.add_edge(v1, v2, True)

    bokeh = BokehGraph(graph)
    bokeh.show()


if __name__ == "__main__":
    main()

