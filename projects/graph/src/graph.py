"""
Simple graph implementation compatible with BokehGraph class.
"""
from random import random, randint


class Vertex:
    def __init__(self, label, height_mod, width_mod):
        self.label = label
        self.edges = set()
        self.x = None
        self.y = None
        self.color = None

    def __str__(self):
        return f'Vertex {self.label}'

    def random_color(self):
        return '#{:02x}{:02x}{:02x}'.format(randint(198, 255),
                                            randint(198, 255),
                                            randint(198, 255))


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """

    def __init__(self, height, width):
        self.vertices = {}
        self.height = height
        self.width = width

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = Vertex(vertex, self.height, self.width)
        else:
            raise Exception('That vertex already exists')

    def add_edge(self, v1, v2):
        if v1 not in self.vertices or v2 not in self.vertices:
            raise Exception('One or both vertices are not in graph.')
        self.vertices[v1].edges.add(v2)
        self.vertices[v2].edges.add(v1)

    def get_nodes(self):
        x = []
        y = []
        for vertex in self.vertices:
            x.append(self.vertices[vertex].x)
            y.append(self.vertices[vertex].y)
        return zip(x, y)

    def get_edges(self):
        s = []
        e = []
        checked = set()
        for vertex, edges in self.vertices.items():
            if vertex not in checked:
                for connection in edges.edges:
                    s.append(vertex)
                    e.append(connection)
                checked.add(vertex)
        return dict(start=s, end=e)

    def get_colors(self):
        colors = []
        for node in self.vertices:
            colors.append(self.vertices[node].color)
        return colors

    def search(self, node, base_x, base_y, type='bfs'):
        if node not in self.vertices:
            raise Exception('Starting point does not exist')

        if type != 'bfs' and type != 'dfs':
            raise Exception('Invalid search type')
        storage = []
        storage.append(node)
        visited = set()
        remove_index = -1 if type == 'dfs' else 0
        base_color = self.vertices[node].random_color()
        count = 1
        x = base_x
        y = base_y
        while storage:
            current = storage.pop(remove_index)
            if current not in visited:
                visited.add(current)
                storage.extend(list(self.vertices[current].edges))
                self.vertices[current].color = base_color
                self.vertices[current].x = x
                self.vertices[current].y = y
                print(x)
                x += (x * -3) + (random() * count)
                print(x)
                y += (y * -3) + (random() * count)
                count += 1
        return visited
