class Vertex:
    def __init__(self, value):
        self.value = value
        self.connections = {}

    def __str__(self):
        return f"{self.value} + connections: {[x.value for x in self.connections]}"

    def add_connection(self, vertex, weight=0):
        self.connections[vertex] = weight

    def get_connections(self):
        return self.connections.keys()

    def get_value(self):
        return self.value

    def get_weight(self, vertex):
        return self.connections[vertex]


class Graph:
    def __init__(self):
        self.vertices = {}
        self.count = 0

    def add_vertex(self, value):
        self.count += 1
        new_vertex = Vertex(value)
        self.vertices[value] = new_vertex
        return new_vertex

    def add_edge(self, vertex1, vertex2, weight=0):
        if not self.vertices.get(vertex1):
            # if vertex1 not in vertices, add it
            self.add_vertex(vertex1)

        if not self.vertices.get(vertex2):
            # if vertex2 not in vertices, add it
            self.add_vertex(vertex2)

        # add connection between vertex1 and vertex2 with the given weight
        self.vertices[vertex1].add_connection(self.vertices[vertex2], weight)

    def get_vertices(self):
        return self.vertices


if __name__ == '__main__':
    g = Graph()
    for i in range(8):
        g.add_vertex(i)

    print(g.vertices)

    g.add_edge(0, 1, 3)
    g.add_edge(0, 7, 2)
    g.add_edge(1, 3, 4)
    g.add_edge(2, 2, 1)
    g.add_edge(3, 6, 5)
    g.add_edge(4, 0, 2)
    g.add_edge(5, 2, 3)
    g.add_edge(5, 3, 1)
    g.add_edge(6, 2, 3)
    g.add_edge(7, 1, 4)

    for i in range(len(g.get_vertices())):
        # print(type(v))
        print(g.vertices[i].get_connections())

        # for w in v.get_connections():
        # print(f"({v.get_value()}, {w.get_value()})")
