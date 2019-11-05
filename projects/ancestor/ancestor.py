"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        self.vertices[v2].add(v1)
           
        """
        Add a directed edge to the graph.
        """
   
    def earliest_ancestor(self , ancestors, starting_node):
        s = Stack()
        visited = set()
        for i in ancestors:
            self.add_edge(i[0] , i[1])
        s.push(starting_node)
        earliestnode = None
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                earliestnode = v
            for next_vertex in self.vertices[v]:
                s.push(next_vertex)
            if earliestnode == starting_node:
                return -1
        return lastnode
    
            
        











if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    print(graph.earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 6))
   

    

    