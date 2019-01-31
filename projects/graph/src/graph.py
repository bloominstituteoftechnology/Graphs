"""
Simple graph implementation
"""
import collections

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = dict()
    
    def add_vertex(self, value):
        self.vertices[value] = set()

    def add_edge(self, vertex1, vertex2):
        self.vertices[vertex1].add(vertex2)
        self.vertices[vertex2].add(vertex1)
    
 
    
    """Write a function within your Graph class that takes takes a starting node as an argument, 
    then performs BFT. Your function should print the resulting nodes in the order they were visited."""
    def bft(self, root):
        # create a seen set and queue
        seen = []
        queue = collections.deque() 
        queue.append(root)

        while queue:
            node = queue.popleft()
            # print(vertex)
            if node not in seen:
                # print(f'visited nodes: {seen}')
                seen.append(node)
                # queue.append(node)
                next_layer = self.vertices[node]

                for vertex in next_layer:
                    if vertex not in queue and vertex not in seen:
                        queue.append(vertex)

        return f'visited nodes: {seen}'


    
    def dft(self, root):
          # create a seen set and queue
        seen = []
        stack = [root]

        while stack:
            node = stack.pop()
            
            if node not in seen:
                print(node)
                seen.append(node)

                next_layer = self.vertices[node]

                for vertex in next_layer:
                    if vertex not in stack and vertex not in seen:
                        stack.append(vertex)

        return f'visited nodes: {seen}'

    def dft_recursive(self, root, seen=[]):
        seen = seen + [root]
        print(root)
        for next_layer in self.vertices[root]:
            if next_layer not in seen:
                seen = self.dft_recursive(next_layer, seen)
        return seen
