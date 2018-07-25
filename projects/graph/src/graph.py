#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""



class Graph:
    # Represent a graph as a dictionary of vertices mapping labels to edges.
    def __init__(self):
        self.vertices = {}  # represent as a dict

    def add_vertex(self, vertex, edges=()):
        if vertex in self.vertices:
            raise Exception('Error - adding vertex that already exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error - cannot have edge to nonexistent vertices')
        self.vertices[vertex] = set(edges) 

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error - vertices to connect not in graph')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def randomize(self, num_vertex, num_edge):
        num_list = []
        for num in xrange(0, num_vertex):
            self.add_vertex(x)
            num_list.append(x)

    def bfs(self, start):
      
        starting = start
        adjacent = list(self.vertices[start])
        visited = []
        queue = []
        queue.append(starting)
        visited.append(starting)
        print(starting)

        while (queue):
            v = queue.pop(0)
            print("visited", type(v))
            print(self.vertices[v])
            for num in list(self.vertices[v]):
                print("visited", num)
                if num in visited:
                    print("testing")
                else:
                    visited.append(num)
                    queue.append(num)
                    
        print(visited)
            
          
        

        

    

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
#graph.add_edge('0', '4')  # No '4' vertex, should raise an Exception!
print(graph.vertices)

