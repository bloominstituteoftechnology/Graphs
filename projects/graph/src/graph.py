"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, label):
        self.label = label
        self.edges = set()

    def __repr__(self):
        return str(self.label)

class Graph:
    def __init__(self):        
        self.vertices = {}        
    
    def add_edge(self, start_index, end_index, bidirectional=True):
        if start_index not in self.vertices or end_index not in self.vertices:
            raise Exception("%s or %s does not exist" %(start_index, end_index))
        else:
            self.vertices[start_index].add(end_index)
            if bidirectional == True:
                self.vertices[end_index].add(start_index)        

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            raise ValueError("That vertex already exists in the graph.")

    def create_random_graph(self, n_verts):
        grid = []
        for i in range(n_verts):
            grid.append(Vertex(str(i)))
        
        for i in range(n_verts - 1):
            if (random.randrange(n_verts) < n_verts // 2):
                if (random.randrange(n_verts) < n_verts // 2):
                    self.add_edge(grid[i].label, grid[i + 1].label, False)
                self.add_edge(grid[i].label, grid[i + 1].label)

        for vert in grid:
            self.add_vertex(vertex)

# Test: 
graph = Graph() # Instantiating an empty graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)

# graph.add_edge('0', '4')

