"""
Simple graph implementation compatible with BokehGraph class.
"""
import random
from queue import PriorityQueue

class Vertex:
    def __init__(self, data, x=None, y=None):
        self.id = data
        self.edges = set()
        if x is None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y is None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y
    def __repr__(self):
        return f"{self.edges}"

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        node = Vertex(vertex)
        self.vertices[vertex] = node

    def add_edge(self, src, dest):
        if src in self.vertices and dest in self.vertices:
            self.vertices[src].edges.add(dest)
            self.vertices[dest].edges.add(src)

    def num_nodes(self):
        num_nodes = 0
        for _ in self.vertices:
            num_nodes += 1
        return num_nodes
    
    def list_nodes(self):
        node_list = []
        for node in self.vertices:
            node_list.append(node)
        return node_list

    def BFS(self, graph, startVert):
        q = PriorityQueue()
        for v in graph.vertices:
            graph.vertices[v].color = 'green'

        graph.vertices[startVert].color = 'purple'
        q.put(startVert)

        while not q.empty():
            u = q.queue[0] # Peek at head of queue, but not dequeue!

            for v in graph.vertices[u].edges:
                if graph.vertices[v].color == 'green':
                    graph.vertices[v].color = 'purple'
                    q.put(v)

            q.get()
            graph.vertices[u].color = 'black'

if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)

    graph.add_edge(0, 1)
    graph.add_edge(0, 3)

    # graph.print_graph()
    print(graph.vertices)

    for key in graph.vertices.keys():
        print(graph.vertices[key].edges)

