"""
Simple graph implementation
"""

from collections import deque
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
    
    def add_edge(self, vertex, vertex_2):
        if vertex in self.vertices and vertex_2 in self.vertices:
            self.vertices[vertex].add(vertex_2)
            # add self.vertices[edge] = vertex <-- undirected edge

    def breadth_first_traversal(self, starting_node):
        q = deque()
        visited = []
        q.append(starting_node)
        while len(q) > 0:
            node = q.popleft()
            visited.append(node)
            print(node)
            for child in self.vertices[node]:
                if child not in visited:
                    q.append(child)
        # return visited
    def depth_first_traversal(self, starting_node):
        stack = []
        visited = []
        stack.append(starting_node)
        while len(stack) > 0:
            node = stack.pop()
            visited.append(node)
            print(node)
            for child in self.vertices[node]:
                if child not in visited:
                    stack.append(child)
        return visited

    def dft_recursive(self, node,visited=None):
        if visited is None:
            visited = []
        if node not in visited:
            visited.append(node)
            print(node)
        for child in self.vertices[node]:
            # if child.value == target
                #return child
            self.dft_recursive(child, visited)

    def bfs_path(self, starting_node, target):
        q = deque()
        visited = []
        q.append([starting_node])
        while len(q) > 0:
            path = q.popleft()
            node = path[-1]
            if node not in visited:
                visited.append(node)
                if node == target:
                    return path
                for child in self.vertices[node]:
                    path_copy = path.copy()
                    path_copy.append(child)
                    q.append(path_copy)
        return None
    def dfs_path(self, starting_node, target):
        stack = []
        visited = []
        stack.append([starting_node])
        while len(stack) > 0:
            path = stack.pop()
            node = path[-1]
            if node not in visited:
                visited.append(node)
                if node == target:
                    return path
                for child in self.vertices[node]:
                    path_copy = path.copy()
                    path_copy.append(child)
                    stack.append(path_copy)
        return None

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('6')
graph.add_vertex('5')
graph.add_vertex('7')
graph.add_vertex('8')
graph.add_vertex('10')
graph.add_vertex('11')
graph.add_vertex('12')
graph.add_vertex('15')
graph.add_vertex('18')
graph.add_vertex('12')
graph.add_vertex('25')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('25', '12')
graph.add_edge('0', '25')
graph.add_edge('1', '2')
graph.add_edge('1', '10')
graph.add_edge('2', '4')
graph.add_edge('2', '5')
graph.add_edge('2', '6')
graph.add_edge('5', '7')
graph.add_edge('5', '8')
graph.add_edge('1', '11')
graph.add_edge('2', '4')
graph.add_edge('2', '6')
graph.add_edge('5', '15')
graph.add_edge('5', '18')


#print(graph.vertices)
#graph.breadth_first_traversal('0')
#graph.depth_first_traversal('2')
#print('recursive:')
#graph.dft_recursive('7')

#Check BFS path
print("BFS path:")
print(graph.bfs_path('0', '4'))
print("DFS path:")
print(graph.dfs_path('0', '4'))
