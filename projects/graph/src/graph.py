import random
from random import sample

class Vertex:
    def __init__(self, label, color='white'):
        self.label = label
        self.color = color
        self.edges = set()
        

    def __repr__(self):
        return str(self.label)
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.found = []
     

    def add_vertex(self, vertex):
        if not isinstance(vertex, Vertex):
            vertex = Vertex(vertex)

        # if vertex not in self.vertices:
            # self.vertices[vertex] = set()
        
        self.vertices[vertex.label] = vertex

    def add_edge(self, start, end, bidirectional=True):
        # if start not in self.vertices:
        #     # raise Exception('Error - vertices not in graph!')
        #     self.add_vertex(start)
        # if end not in self.vertices:
        #     self.add_vertex(end)
        # print(start.edges)
        # print(type(start))
        self.vertices[start.label].edges.add(end)
        if bidirectional:
            self.vertices[end.label].edges.add(start)

    # TODO:
    ######## RANDOMIZED GRAPH PRODUCTION IN PROGRESS ######
    # def create_vertices_and_edges(self, num_vertices):
    #     grid = []
    #     for i in range(num_vertices):
    #         grid.append(Vertex(str(i)))
    #     # print(grid) // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] <-- each num corresponds to a label on a vertex
    #     for i in range(num_vertices - 1):
    
    def bfs(self, start):
        print("---------------------BFS WAS CALLED---------------------")
        random_color = '#' + \
            ''.join([random.choice('0123456789ABCDEF') for j in range(8)])


        queue = []
        found2 = [] 

        queue.append(start)
        found2.append(start)
        self.found.append(start)

        start.color = random_color
        
        while (len(queue) > 0):
            v = queue[0]
            print(str(v) + ' vertex')

            for e in v.edges:
                print(str(e) + ' edge')
                
                if e not in self.found:   # // CULPRIT: found keeps resetting each time func runs??
                    e.color = random_color

                    self.found.append(e)
                    found2.append(e)
                    queue.append(e)

            queue.pop(0)  
            for v in found2:
                print(v.color)
        print(str(found2) + ' found list')
        print(str(self.found) + ' SELF.FOUND')        
        return found2

    def get_connected_components(self):
      
        searched = []
        
        # print(self.vertices.items())
        for index, vertex in self.vertices.items():
            if vertex not in searched:
                # print(vertex)
                # searched + (self.bfs(vertex)) # DON'T USE THIS..returns empty searched list
                searched.append(self.bfs(vertex))
                
        print(searched) 
        return searched 
                
    def random_graph(self, num_vertices, num_edges):
        # Add appropriate number of vertices
        for num in range(num_vertices):
            self.add_vertex((str(num)))

        # Add random edges between vertices
        for _ in range(num_edges):
            # vertices = sample(self.vertices.keys(), 2)
            tup = sample(self.vertices.keys(), 2)
            # TODO check if edge already exists
            v0 = Vertex(str(tup[0]))
            v1 = Vertex(str(tup[1]))
            # print(type(v0))
            self.add_edge(v0, v1)




# graph = Graph()  # Instantiate your graph



# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# graph.add_edge('0', '5')
# print(graph.vertices)

