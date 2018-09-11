"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex in self.vertices:
            print("That vertex already exists")
            return False
        else:
            self.vertices[vertex] = set()

    def add_edge(self, startpoint, endpoint):
        if startpoint not in self.vertices or endpoint not in self.vertices:
            print("Invalid start or endpoint")
            return False
        else:
            self.vertices[startpoint].add(endpoint)
            self.vertices[endpoint].add(startpoint)

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

# vertices = {
#     0: {1,3},
#     1: {0,3,4},
#     2: {4},
#     3: {1,0,5},
#     4: {1,2}
#     5: {3}
# }

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')

graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('4', '2')
graph.add_edge('1', '4')
graph.add_edge('5', '3')
graph.add_edge('6', '3')
graph.add_edge('7', '4')

# print('vertices',graph.vertices)
# print('values',graph.vertices.values())
graph.breadth_first_for_each('0')
graph.depth_first_for_each('0')
