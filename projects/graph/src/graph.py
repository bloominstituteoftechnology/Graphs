"""
Simple graph implementation compatible with BokehGraph class.
"""

class Node:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        node = Node(vertex)
        self.graph[vertex] = node

    def add_edge(self, src, dest):
        node = self.graph[src]
        node.next = self.graph[dest]

    def print_graph(self):
        for key in self.graph:
            print("Adjacency list of vertex {}\n head".format(key), end="")
            temp = self.graph[key]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)

    graph.add_edge(0, 1)
    graph.add_edge(0, 3)

    graph.print_graph()