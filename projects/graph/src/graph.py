"""
Simple graph implementation compatible with BokehGraph class.
"""

# x = [1, 2, 3, 4, 5]
# y = [6, 7, 2, 4, 5]
# # output to static HTML file
# output_file("graph.html")

# # create a new plot with a title and axis labels
# p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# # add a line renderer with legend and line thickness
# p.line(x, y, legend="Temp.", line_width=2)

# # show the results
# show(p)


# output_file("graph.html")

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)


# class MatrixGraph:
#     """ Adjacency Matrix Represeation of a graph"""
#     def __init__(self, num_vertices):
#         """edges"""
#         self.matrix  = [[0] * num_vertices] * num_vertices
#         self.vertices = [Vertex(str(i)) for i in range(num_vertices)]
        
#     def add_edge(self, start_index, end_index, bidirectional=True):
#         """ Add an edge from start vertex to end vertex. """
#         self.matrix[start_index][end_index] = 1
#         """ to be bidirectional """
#         if bidirectional:
#             self.matrix[end_index][end_index] = 1
        
# class Vertex:
#     def __init__(self, label):
#         self.label = label
#         self.edges = set()

# class ListGraph:
#     def __init__(self):
#         self.vertices = set()        
        
        
        
        
        
        
        
        # graph = {
#     '0': {'1', '3'},
#     '1': {'0'},
#     '2': set(),
#     '3': {'0'}
# }
        
        
        
        
        
        
        
        
        
        
        
        
        


