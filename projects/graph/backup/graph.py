"""
Simple graph implementation compatible with BokehGraph class. // No Bokeh in this???
"""
from queue import Queue 
from stack import Stack

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, new_vertex):
        self.vertices[new_vertex] = set()

    def add_edge(self, vertex_a, vertex_b):
        self.vertices[vertex_a].add(vertex_b)
        self.vertices[vertex_b].add(vertex_a)

    def add_directed_edge(self, vertex_start, vertex_end):
        self.vertices[vertex_start].add(vertex_end)
    
    def bft(self, starting_vert):

        queue = Queue()
        queue.enqueue(starting_vert) 
        visited = set() 

        while queue.len() > 0: 
            cur_vert = queue.dequeue()
            print(f'cur_vert: {cur_vert}')
            visited.add(cur_vert)

            for vert in self.vertices[cur_vert]:
                if vert is not None:
                    if not vert in visited:
                        queue.enqueue(vert)

    def dft(self, starting_vert):

        stack = Stack()
        stack.add_to_tail(starting_vert) 
        visited = set() 

        while stack.len() > 0: 
            cur_vert = stack.remove_from_tail()
            # if cur_vert is in visited, just pass
            if cur_vert in visited:
                pass

            else:
                visited.add(cur_vert)
                print(f'cur_vert: {cur_vert}')

                for vert in self.vertices[cur_vert]:
                    if vert is not None:
                        if not vert in visited:
                            stack.add_to_tail(vert)

                            





graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_edge('1', '4')
graph.add_edge('1', '3')
graph.add_edge('4', '7')
graph.add_directed_edge('0', '1')
graph.add_directed_edge('4', '2')
graph.add_directed_edge('2', '5')
graph.add_directed_edge('4', '6')
graph.add_directed_edge('6', '7')
graph.dft('0')
