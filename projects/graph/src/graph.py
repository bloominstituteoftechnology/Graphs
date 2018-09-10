"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex, edges=()):
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end)

        if bidirectional:
            self.vertices[end].add(start)

    
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