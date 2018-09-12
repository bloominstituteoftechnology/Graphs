from sys import argv
from graph import Graph
from draw import BokehGraph

def main():
    graph = Graph()
    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show()

if __name__ == '__main__':
    main()
