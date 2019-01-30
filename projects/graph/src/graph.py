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
    
    def add_edge(self, origin, target):
        if origin == target:
            print('Origin must not match target.')
        if origin in self.vertices and target in self.vertices:
            self.vertices[origin].add(target)
        else:
            print('One of the provided vertices does not exist.')

    # Breadth First Traversal
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

    # Depth First Traversal
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

    # Recursive Depth First Traversal
    def dft_r(self, vertex, cache = set()):

        # Print the vertex
        print(vertex)

        # Add vertex to cache
        cache.add(vertex)

        # Check all edges of current vertex 
        for i in self.vertices[vertex]:

            # with vertices not already checked
            if i not in cache:
                self.dft_r(i, cache)

    # Breadth First Search
    def bfs(self, origin, target):

        # Check if target matches the origin
        if target == origin:
            return 'Self matches origin.'
        
        # Keep track of vertices to be visited
        queue = [origin]

        # Keep track of the paths need to reach vertices
        paths = {origin:[origin]}

        while len(queue) > 0:
            
            # Add all edges of given vertex to queue
            for i in self.vertices[queue[0]]:

                # If vertex has not been visited, cache its path
                if i not in paths:
                    paths[i] = list(paths[queue[0]])
                    paths[i].append(i)
                    queue.append(i)

                    # If vertex matches target, return target
                    if i == target:
                        return paths[i]

            # Remove last item checked
            queue.pop(0)
        
        # Return a message if target was not found
        return 'A path to the given target vertex could not be found.'
                


    # Depth First Search


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

# print(graph.vertices)
# graph.add_edge('0', '4')

# graph.bft('0')
# print('')
# graph.dft('0')
# print('')
# graph.dft_r('0')

print(graph.bfs('3', '2'))