"""
Simple graph implementation compatible with BokehGraph class.
"""
import random
from queue import PriorityQueue
from random import sample

class Vertex:
    def __init__(self, data, x=None, y=None, component=-1):
        self.id = data
        self.edges = set()
        self.color = 'white'
        self.component = component
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
    
    def BFT(self, startVert):
        q = PriorityQueue()
        visited = []
        for v in self.vertices:
            self.vertices[v].color = 'white'
        
        # print('****', self.vertices[startVert].color)
        self.vertices[startVert].color = 'red'
        q.put(startVert)

        while not q.empty():
            u = q.queue[0]
            visited.append(self.vertices[u])
            # print("edges", self.vertices[u].edges)
            for v in self.vertices[u].edges:
                if self.vertices[v].color == 'white':
                    self.vertices[v].color = 'red'
                    if v not in visited:
                        q.put(v)
            q.get()
            self.vertices[u].color = 'blue'
        return visited

    def connected_components(self):
        # connected_components = dict()
        # for v in self.vertices:
        #     # print(v)
        #     self.vertices[v].color = 'white'
        #     if self.vertices[v] not in connected_components:
        #         connected_components.update({f"{self.vertices[v].id}": self.BFT(self.vertices[v].id)})
        #     if self.vertices[v].color == 'white':
        #         self.vertices[v].color = 'green'
        # print("CC", connected_components)
        # return connected_components

        connected_components = set()
        current_component = 0

        for v in self.vertices:
            if self.vertices[v] not in connected_components:
                reachable = self.BFT(self.vertices[v].id)
                print('reachable', reachable)
                for other_v in reachable:
                    # print(other_v.color)
                    other_v.component = current_component
                current_component += 1
                connected_components.update(reachable)
        self.components = current_component
        return connected_components

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

