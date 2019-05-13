"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        pass  # TODO
    def add_edge(self, v1, v2):
        pass  # TODO




if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_vertex('5')
    graph.add_vertex('6')
    graph.add_vertex('7')
    graph.add_edge('5', '3')
    graph.add_edge('6', '3')
    graph.add_edge('7', '1')
    graph.add_edge('4', '7')
    graph.add_edge('1', '2')
    graph.add_edge('7', '6')
    graph.add_edge('2', '4')
    graph.add_edge('3', '5')
    graph.add_edge('2', '3')
    graph.add_edge('4', '6')
    print(graph.vertices)
