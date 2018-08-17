"""
Simple graph implementation compatible with BokehGraph class.
"""
from draw import BokehGraph
from random import random

class Vertex:
    def __init__(self, label, color="gray", component=-1, **pos):
        self.label = label
        self.color = color
        self.pos = pos
        self.component = component
        self.edges = set()
        

    # Use the str method instead
    def __str__(self):
        if not self.pos:
            pos = dict(x=None, y=None)
        else:
            pos = self.pos
        return "Vartex is {}, position at ({}, {}), color is {} and has edges  {}".format(self.label, pos['x'], pos['y'], self.color, self.edges)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex):
        if not isinstance(vertex, Vertex):
            vertex = Vertex(vertex)

        if vertex.label in self.vertices:
            return False  # ignores it

        self.vertices[vertex.label] = vertex
        return True  # added

    def add_edge(self, start, end, multidirectional=True):

        if isinstance(start, Vertex):
            start = start.label
        if isinstance(end, Vertex):
            end = end.label
        # adding the start point if it doesn't exist in the vertices list/array already
        if start not in list(self.vertices.keys()):
            self.add_vertex(Vertex(start))
        # adding the end point if it doesn't exist in the vertices list/array already
        if end not in list(self.vertices.keys()):
            self.add_vertex(Vertex(end))

        self.vertices[start].edges.add(self.vertices[end])
        if multidirectional:
            self.vertices[end].edges.add(self.vertices[start])

    # # breadth first search
    # def bfs(self, start, target=None):
    #     queue = [start]
    #     visited = set()

    #     while queue:
    #         current = queue.pop(0)
    #         if current == target:
    #             break
    #         visited.add(current)
    #         # try to add possible unvisited vertices to the queue
    #         queue.extend(self.vertices[current] - visited)

    #     return visited

    # # depth first search    
    # def dfs(self, start, target=None):
    #     stack = [start]
    #     visited = set()

    #     while stack:
    #         current = stack.pop()
    #         if current == target:
    #             break
    #         visited.add(current)
    #         # try to add possible unvisited vertices to the queue
    #         stack.extend(self.vertices[current] - visited)

    #     return visited

    def search(self, start, target=None, method='dfs'):
        #search the graph using either BFS or DFS 
        queueOrStack = [start]
        popIndex = 0 if method == 'bfs' else -1
        visited = set()

        while queueOrStack:
            current = queueOrStack.pop(popIndex)
            if current == target:
                break
            visited.add(current)
            # try to add possible unvisited vertices to the queue
            queueOrStack.extend(self.vertices[current] - visited)

        return visited


    def find_components(self):
        # identify components and update vertex component id's
        visited = set()
        current_component = 0


        for vertex in self.vertices:
            if vertex not in visited:
                reachableVertices = self.search(vertex)      
                for other_vertex in reachableVertices:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachableVertices)
        self.components = current_component

     # creating random graph part       
    def create_random_graph(self, n_verts):
        # create some verts and put them in a grid
        grid = []
        
        for i in range(n_verts):
            grid.append(Vertex(str(i)))
        
        #randomly looping through verts and randomly connecting it to the next one with randomized mulidirection
        for i in range(n_verts - 1):
            if(random.randrange(n_verts) < n_verts // 2):
                if(random.randrange(n_verts) < n_verts // 2):
                    self.add_edge(grid[i].label, grid[i+1].label, False)
                self.add_edge(grid[i].label, grid[i+1].label)
        
        for vert in grid:
            self.add_vertex(vert)


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)

b = BokehGraph(graph)
b.show()








            
