"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, label):
        if label in self.vertices:
            print('Already accounted for')
        else:
            self.vertices[label] = set()
        
    def add_edge(self, label, destination):
        if label in self.vertices:
            if destination in self.vertices:
                self.vertices[label].add(destination)
            else:
                print('No destination')
        else:
            print('No vertex')

    def bfs(self, start_node):
        # create a queue
        queue = []
        # create a visited list
        visited = []
        # put the start node in the queue
        queue.append(start_node)
        # while queue is not empty...
        while len(queue) > 0:
            # remove node from queue
            current = queue.pop(0)
            # check if it's visited
            if current not in visited:
                # if not, mark node as visited
                visited.append(current)
            # then put all children in queue
            for i in self.vertices[current].edges:
                if i not in visited and i not in queue:
                    queue.append(i)
        return visited
    
    def dfs(self, start_node):
        stack = []
        visited = []
        queue.append(start_node)
        while len(queue) > 0:
            current = queue.pop()
            if current not in visited:
                visited.append(current)
            for i in self.vertices[current].edges:
                if i not in visited and i not in queue:
                    queue.append(i)
        return visited


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
