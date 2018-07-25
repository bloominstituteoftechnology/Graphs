#!/usr/bin/python

from draw import BokehGraph

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        

    def add_edge(self,start,end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error - vertices not in graph!')
        else:
            self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def add_vertex(self, vertex):
        #if not hasattr(vertex, self):
            #raise Exception('NOT a vertex!!')
        self.vertices[vertex] = set()

#creating main method per AG

def main():
    graph = Graph()  # Instantiate your graph (from repo)
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
    graph.add_edge('0', '3')
    graph.add_edge('4', '3')
    graph.add_edge('1', '3')

    bg = BokehGraph(graph)
    bg.show()

if __name__ == "__main__":
    main()


