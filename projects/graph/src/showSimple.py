from graph import Graph
from draw import BokehGraph

2 +  3
graph = Graph()  # Instantiate your graph
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
graph.add_edge('1', '8')
graph.add_edge('1', '2')
graph.add_edge('2', '4')
graph.add_edge('2', '5')
graph.add_edge('3', '6')
graph.add_edge('3', '5')
graph.add_edge('3', '7')
graph.add_edge('4', '5')
graph.add_edge('1', '9')
graph.add_edge('0', '3')
graph.bfs('3')
print(graph.vertices)

bokeh = BokehGraph(graph)

bokeh.randomize()

bokeh.show()