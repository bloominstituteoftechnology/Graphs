"""
Simple graph implementation
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        pass  # TODO
        self.vertices = {}
    
    def add_vertex(self, value):
        if value not in self.vertices:
            self.vertices[value] = set()
    
    def add_edge(self, vertex, target):
        # print(self.vertices)
        # print(self.vertices[vertex])
        # print(hasattr(self.vertices, vertex))
        if vertex in self.vertices and target in self.vertices:
            self.vertices[vertex].add(target)
        else:
            print('One of the provided vertices does not exist.')

    def bft(self, vertex):
        # Keep track of vertices to be visited
        queue = [vertex]

        # Keep track of vertices visited
        visited = set(vertex)

        while len(queue) > 0:
            # Add all edges of given vertex to queue
            for i in self.vertices[queue[0]]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)

            # Print and Remove current vertex
            print(queue.pop(0))

    def dft(self, vertex):
        # Keep track of vertices to be visited
        stack = [vertex]

        # Keep track of vertices visited
        visited = set(vertex)

        while len(stack) > 0:
            # Print and Remove current vertex
            current_vertex = stack.pop()
            print(current_vertex)

            # Add all edges of given vertex to queue
            for i in self.vertices[current_vertex]:
                if i not in visited:
                    visited.add(i)
                    stack.append(i)


# Test
graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('5')
graph.add_vertex('12')
graph.add_vertex('99')
graph.add_vertex('14')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('1', '0')
graph.add_edge('3', '0')
graph.add_edge('3', '12')
graph.add_edge('12', '5')
graph.add_edge('1', '5')
graph.add_edge('5', '1')
graph.add_edge('5', '2')
graph.add_edge('12', '14')

print(graph.vertices)
# graph.add_edge('0', '4')

graph.bft('0')
print('')
graph.dft('0')