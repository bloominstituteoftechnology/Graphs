#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    """Represent a vertex with a label and possible connected component."""
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end)

        if bidirectional:
            self.vertices[end].add(start)

    def search(self, start, target=None, method='dfs'):
        quack = [start]
        pop_index = 0 if method == 'bfs' else -1
        visited = set()

        while quack:
            current = quack.pop(pop_index)
            if current == target:
                break
            visited.add(current)
            quack.extend(self.vertices[current] - visited)

        return visited

def main():
    graph = Graph()  
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')    
    graph.add_edge('0', '1', False)
    graph.add_edge('2', '3')
    graph.add_edge('2', '1')    
    print(graph.vertices)

if __name__ == '__main__':
    main()