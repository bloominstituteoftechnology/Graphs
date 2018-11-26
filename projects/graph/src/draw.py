"""
General drawing methods for graphs using Bokeh.
"""

from graph import Graph
# from bokeh.io import show, output_file
# from bokeh.plotting import figure
# from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
#                           ColumnDataSource)
                        


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self):
        pass  # TODO

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('4', '3')
graph.add_edge('6', '3')
graph.add_edge('6', '1')
graph.add_edge('5', '0')
graph.add_edge('4', '1')




graph.bfs('7')
graph.dfs('7')
print(graph.vertices)
