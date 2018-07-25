"""
Simple graph implementation compatible with BokehGraph class."""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        pass  # TODO
        self.vertices = {}

    def add_vertex(self, v):
        if v not in self.vertices:
            self.vertices[v] = set()
        else:
            raise ValueError("vertex already exists in the Graph")

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception("%s or %s does not exist" %(start, end))
        else:
            self.vertices[start].add(end)
            if bidirectional == True:
                self.vertices[end].add(start)



#     g = Graph()
#     g.add_vertex('2')
#     g.add_vertex('3')
#     g.add_vertex('8')
#     g.add_edge('2','3')
#     g.add_edge('2','8')
#     g.add_edge('8','3')


# # print(g.vertices)





