"""
Simple graph implementation compatible with BokehGraph class. // No Bokeh in this???
"""
from queue import Queue 

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, new_vertex):
        self.vertices[new_vertex] = set()

    def add_edge(self, vertex_a, vertex_b):
        self.vertices[vertex_a].add(vertex_b)
        self.vertices[vertex_b].add(vertex_a)
    
    def bft(self, starting_vert):

        queue = Queue()
        queue.enqueue(starting_vert) # Why does this have to be a separate step from instantiation?
        visited = set() 

        while queue.len() > 0: 
            cur_vert = queue.dequeue()
            print(f'\ncur_vert: {cur_vert}')
            visited.add(cur_vert)

            for vert in self.vertices[cur_vert]:
                if vert is not None:
                    if not vert in visited:
                        queue.enqueue(vert)


graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.bft('0')
