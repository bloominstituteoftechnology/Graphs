"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, vertices, probability):
        self.vertices = {}
        self.total_v = int(vertices)
        self.prob = float(probability)

    def add_vertex(self, label):
        #check if an object with label already exists
        if label in self.vertices:
            raise ValueError(f"Duplicate vertex '{label}' found")
        #create new vertex object with the label passed to function
        self.vertices[label] = set()

    def add_directed_edge(self, start, end):
        if start not in self.vertices:
            raise ValueError(f"Vertex '{start}' not found")
        if end not in self.vertices:
            raise ValueError(f"Vertex '{end}' not found")
        self.vertices[start].add(end)

    def add_undirected_edge(self, start, end):
        if start not in self.vertices:
            raise ValueError(f"Vertex '{start}' not found")
        if end not in self.vertices:
            raise ValueError(f"Vertex '{end}' not found")
        if self.vertices[start] == end or self.vertices[end] == start:
            print('Edge already exists.')
            return
        self.vertices[start].add(end)
        self.vertices[end].add(start)

    def generate_vertices(self):
        for i in range(self.total_v):
            label = 'v'+ str(i)
            self.add_vertex(label)
    
    def generate_edges(self):
        count_chance = 0
        count_here = 0
        vertices = list(self.vertices.keys())
        for v in vertices:
            for k in [i for i in vertices if i != v]:
                chance = random.random()
                print(chance, self.prob)
                count_chance += 1 if chance <= self.prob else 0
                if chance < self.prob and v not in self.vertices[k]:
                    count_here += 1
                    self.add_undirected_edge(v, k) 
        print(count_chance, count_here)
        # edges = []
        # while True:
        #     start = vertices[random.randint(0, len(vertices)-1)]
        #     end = vertices[random.randint(0, len(vertices)-1)]
        #     chance = random.random()
        #     if start!=end and [start, end] not in edges and [end, start] not in edges and chance <= self.prob:
        #         edges.append([start, end])
        #         if len(edges) == self.total_e:
        #             break

        # for edge in edges:
        #     if not self.directed:
        #         self.add_undirected_edge(edge[0], edge[1])

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
                
            
        