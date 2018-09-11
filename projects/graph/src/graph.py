"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.verts = {}

    def add_vertex(self, label):
        if self.verts.get(label) == None:
            self.verts[label] = []
        else:
            return 'vertex already exists'

    def add_edge(self, x, y):
        if self.verts.get(x) == None:
            return f'{x} is not a vertex on the graph'
        elif self.verts.get(y) == None:
            return f'{y} is not a vertex on the graph'
        else:
            self.verts[x].append(y)
            self.verts[y].append(x)

    def breadth_first_for_each(self, start):
        queue = [] # setup a que to check nodes
        queue.append(start) # first/root node
        visited = []
        while len(queue) > 0:
            current = queue.pop(0) # first in que pulled out
            visited.append(current) #push into visited
            for edge in self.vertices[current]:  #look at connections,
                if edge not in visited and edge not in queue:    # if the connected node isn't visited,
                    queue.append(edge)   # then enqueue it
        print(visited)


    def depth_first_for_each(self, start):
        stack = [] # setup a que to check nodes
        stack.append(start) # first/root node
        visited = []
        while len(stack) > 0:
            current = stack.pop() # first in que pulled out
            visited.append(current) #push into visited
            for edge in self.vertices[current]:  #look at connections,
                if edge not in visited and edge not in stack:    # if the connected node isn't visited,
                    stack.append(edge)   # then enqueue it
        print(visited)

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.verts)
