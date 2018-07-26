#!/usr/bin/python

from draw import BokehGraph

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, label):
        self.vertices[label] = set()

    def add_edge(self, start, end, bidirectional=True):
        if start in self.vertices and end in self.vertices:
            self.vertices[start].add(end)
            if bidirectional:
                self.vertices[end].add(start)
        else:
            raise ValueError("Please provide start and end vertices that exist.")

    def breadth_first(self, vertex, callback):
        queue = [vertex]
        visited = set()
        while queue:
            current = int(queue.pop(0))
            callback(current)
            visited.add(current)
            for i in self.vertices[current]:
                if i not in visited:
                    queue.append(i)


def main():
    graph = Graph()
    graph.add_vertex("0")
    graph.add_vertex("1")
    graph.add_vertex("2")
    graph.add_vertex("3")
    graph.add_vertex("4")
    graph.add_vertex("5")
    graph.add_vertex("6")
    graph.add_vertex("7")
    graph.add_vertex("8")
    graph.add_vertex("9")
    graph.add_vertex("10")
    graph.add_vertex("11")
    graph.add_vertex("12")
    graph.add_edge("0", "1")
    graph.add_edge("0", "3", False)
    graph.add_edge("0", "2", False)
    graph.add_edge("10", "8", False)
    graph.add_edge("7", "6")
    graph.add_edge("11", "12", False)
    graph.add_edge("11", "0", False)

    b = BokehGraph(graph)
    b.show()


if __name__ == "__main__":
    main()
