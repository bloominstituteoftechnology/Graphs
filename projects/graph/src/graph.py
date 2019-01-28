from collections import deque
"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
    
    def add_edge(self, v1, v2):
        if v1 in vertices and v2 in vertices:
            self.vertices[v1].add[v2]
            self.vertices[v2].add[v1]
            return 
        else: 
            print("At least one vertex does not exist.")
            return 


# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(graph.vertices)

    def bft(self, s):
        #create a queue
        q = deque()
        visited = set()
        #mark the first node as visited
        #enqueue the starting node
        q.append(s)
        visited[s] = True
        #while the queue is not empty
        while q:
            #dequeue a node from the queue
            dequeue = q.pop(0)
            #mark that node as visited
            if dequeue not in visited:
                visited.add(dequeue)
            #enqueue all of its children that have not already been added to queue
            for i in self.vertices(i):
                if i not in visited:
                    q.append(i)

        return visited