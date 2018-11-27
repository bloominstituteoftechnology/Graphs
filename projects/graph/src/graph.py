"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, label):
        if label in self.vertices:
            raise "Vertex already exists.", label
        else:
            self.vertices[label] = {'edges':set()}
    
    def add_edge(self, label, destination):
        if label in self.vertices:
            if destination in self.vertices:
                self.vertices[label]['edges'].add(destination)
                self.vertices[destination]['edges'].add(label)
            else:
                raise 'Vertex does not exist.', destination
        else:
            raise 'Vertex does not exist.', label
    
    def breadth_first_traversal(self, start_vertex):
        print('breadth first traversal')
        for vertex in self.vertices:
            self.vertices[vertex]['color'] = 'white'
        self.vertices[start_vertex]['color'] = 'grey'
        queue = [start_vertex]
        while len(queue)>0:
            first = queue[0]
            print(first)
            for vertex in self.vertices[first]['edges']:
                if self.vertices[vertex]['color'] == 'white':
                    self.vertices[vertex]['color'] = 'grey'
                    queue.append(vertex)
            queue.pop(0)
            self.vertices[first]['color'] = 'black'
    
    def depth_first_traversal(self, start_vertex):
        print('depth first traversal')
        for vertex in self.vertices:
            self.vertices[vertex]['color'] = 'white'
        self.vertices[start_vertex]['color'] = 'grey'
        stack = [start_vertex]
        while len(stack)>0:
            first = stack.pop()
            print(first)
            for vertex in self.vertices[first]['edges']:
                if self.vertices[vertex]['color'] == 'white':
                    self.vertices[vertex]['color'] = 'grey'
                    stack.append(vertex)
            self.vertices[first]['color'] = 'black'

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('1','2')
print(graph.vertices)
graph.breadth_first_traversal('0')
graph.depth_first_traversal('0')