from draw import BokehGraph
from graph import Graph
from sys import argv

def main():
    graph = Graph()
    bokeh = BokehGraph(graph)
    bokeh.show()
    