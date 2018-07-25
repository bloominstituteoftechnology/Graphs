import random


class Vertex:
    def __init__(self, label, color="gray", **pos):
        self.label = label
        self.color = color
        self.pos = pos
        self.edges = set()

    '''
    def __repr__(self):
        return str(self.label)
    '''

    # Use the str method instead
    def __str__(self):
        if not self.pos:
            pos = dict(x=None, y=None)
        else:
            pos = self.pos
        return "Vartex is {}, position at ({}, {}), color is {} and has edges  {}".format(self.label, pos['x'], pos['y'], self.color, self.edges)


class Graph:
    def __init__(self):
        self.vertices = {}

    # we can see what properties are on the Graph
    def __str__(self):
        return str(self.vertices)

    def add_edge(self, start, end, bidirectional=True):
        """ And an edge (default bidirectional) between two vertices"""

        # Change this so that if not in vertices, just add it
        '''
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Vertices to connect not in graph!")
        self.vertices[start].add(end)
        '''
        # using the key, if we are passed an object just get the key

        if isinstance(start, Vertex):
            start = start.label

        if isinstance(end, Vertex):
            end = end.label

        # add start if not in vertices
        if start not in list(self.vertices.keys()):
            self.add_vertex(Vertex(start))

        # add end if not in vertices
        if end not in list(self.vertices.keys()):
            self.add_vertex(Vertex(end))

        self.vertices[start].edges.add(self.vertices[end])
        if bidirectional:
            self.vertices[end].edges.add(self.vertices[start])

    def add_vertex(self, vertex):

        if not isinstance(vertex, Vertex):
            vertex = Vertex(vertex)

        if vertex.label in self.vertices:
            return False  # ignores it

        self.vertices[vertex.label] = vertex
        return True  # added

    # Create a random graph
    def create_vertices_and_edges(self, n_verts):
        # create verts and put them in a grid
        grid = []
        for i in range(n_verts):
            grid.append(Vertex(str(i)))

        # randomly loop through verts and randomly connect it to the next one, passing in the random bidirection
        for i in range(n_verts - 1):
            if (random.randrange(n_verts) < n_verts // 2):
                if(random.randrange(n_verts) < n_verts // 2):
                    self.add_edge(grid[i].label, grid[i+1].label, False)
                self.add_edge(grid[i].label, grid[i+1].label)

        for vert in grid:
            self.add_vertex(vert)

    # for debugging only

    def debug_create_test_data(self):

        v0 = Vertex("0")
        self.add_vertex(v0)
        self.add_vertex("1")
        self.add_vertex("2")

        self.add_vertex("3")
        self.add_vertex("4")
        self.add_vertex("5")
        self.add_vertex("6")

        v7 = Vertex("7")
        v8 = Vertex("8")
        v9 = Vertex("9")
        self.add_vertex(v7)
        self.add_vertex(v8)
        self.add_vertex(v9)
        self.add_vertex("10")

        self.add_edge("0", "1")
        self.add_edge("5", "1")
        self.add_edge("7", "5", False)

    def bfs(self, start):
        random_color = '#' + \
            ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        queue = []
        found = []
        queue.append(start)
        found.append(start)

        start.color = random_color

        while (len(queue) > 0):
            v = queue[0]
            for edge in v.edges:
                if edge not in found:
                    found.append(edge)
                    queue.append(edge)
                    edge.color = random_color

            queue.pop(0)  # TODo look at collections.dequeue
        return found

    # Get the connected components
    def get_connected_components(self):
        # Connected Components
        # Go to the next unfound vertex in graph vertices and call BFS on it
        # Go to step 1 until we get to the end of the array(loop)

        searched = []

        for index, vertex in self.vertices.items():
            if vertex not in searched:
                searched.append(self.bfs(vertex))

        return searched