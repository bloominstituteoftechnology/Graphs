class Vertex:
    def __init__(self, label, color="white"):
        self.label = label
        self.edges = set()
        self.color = color

    def __repr__(self):
        return str(self.label)

class BFSGraph:
    
    queue = []

    def __init__(self):
        self.vertices = set()

    def add_vertex(self, vertex):
        self.vertices..add(vertex)
        queue.enqueue(self.vertices.add(vertex)

    def add_edge(self, start, end, bidirectional=True):

        start.edges.add(end)
        if bidirectional:
            end.edges.add(start)

    def breadth_first_search(self, startVertex):

        startVertex.color = "gray"
        queue.enqueue(startVertex)

        while queue is not queue.Empty():
            for next_vertex in queue[1:]:
                if next_vertex.color == white:
                    next_vertex.color = "gray"
                    queue.enqueue(next_vertex) 



