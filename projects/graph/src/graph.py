"""
Simple graph implementation
"""

from collections import deque

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # add a dictionary of vertices
        self.vertices = {}
    # placeholders for add_vertex and add_edge methods
    # add_vertex needs only a vertex, while add_edge needs both a vertex and edge
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].add(vertex2)
        elif vertex not in self.vertices:
            raise Exception(f'There is no edge to vertex {vertex}! Please try again.') # will revisit this

    # breadth-first traversal method
    def bft(self, start):
        x = deque()
        visited = []
        x.append(start)

        """
        popleft() covers what we need to do for breadth-first, we keep moving along the same level
        the visited node is added to the 'visited' list
        if after the breadth-wide search a node has an unvisited child, we append the child to the list as well
        """

        while len(x) > 0:
            node = x.popleft()
            visited.append(node)
            for child in node:
                if child not in visited:
                    x.append(child)
        return visited
    
    # depth-first traversal with stack
    def dft(self, start):
        stack = []
        visited = []
        stack.append(start)

        """
        for depth-first we'll use pop() instead since we're moving 'vertically' rather than shifting left/right
        once the node is popped it is added to the 'visited' list
        move to the children of the nodes afterward

        """
        while len(stack) > 0:
            node = stack.pop()
            visited.append(node)
            for child in self.vertices[node]:
                if child not in visited:
                    stack.append(child)
        return visited

    def dft_recur(self, node, visited = None):
        if visited is None:
            visited = []
        if node not in visited:
            visited.append(node)
        for child in self.vertices[node]:
            self.dft_recur(child, visited)

    # searches - will require a target parameter unlike traversals

    def bfs(self, start, target):
        x = deque()
        visited = []
        x.append([start])
    """
    we can use popleft() again here for breadth-first search
    since this is a search rather than a traversal we'll need to return a path as well
    general BFS searching logic should apply in the same way that it did earlier
    """
        while len(x) > 0:
            path = q.popleft()
            node = path[-1]
            if node not in visited:
                visited.append(node)
                if node == target:
                    return path # search is over when node matches target
                for child in self.vertices[node]:
                    newpath = path.copy()
                    newpath.append(child)
                    x.append(newpath)
        return None

    def dfs(self, start, target):
        stack = []
        visited = []
        stack.append([start])

        """
        logic here should be more or less the same as the bfs method
        main difference is using pop() rather than popleft() to move vertically instead of horizontally
        """
        while len(stack) > 0:
            path = stack.pop()
            node = path[-1]
            if node not in visited:
                visited.append(node)
                if node == target:
                    return path
                for child in self.vertices[node]:
                    newpath = path.copy()
                    newpath.append(child)
                    stack.append(newpath)
        return None

        
# testing

graph = Graph() 
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
# test case for exception
# graph.add_edge('0', '4') # should cause an error
print(graph.bft(graph.vertices['0']))
print(graph.dft(graph.vertices['0']))