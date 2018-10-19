"""
Simple graph implementation compatible with BokehGraph class.
"""







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
        
        
        
# graph = {
#     '0': {'1', '3'},
#     '1': {'0'},
#     '2': set(),
#     '3': {'0'}
# }
def __repr__(self):
        return f"{self.edges}"



class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    #constructor
    def __init__(self): #self mandatory
        #creating the space for the nodes
        self.vertices = {}

    
    
    #creating vertices
    def add_vertex(self, vertex_id):
        #TODO
        self.vertices[vertex_id] = set()
    
    def add_edge(self, v1, v2):
        self.edges = set()
        #if the vertices are in 
        if v1 in self.vertices and v2 in self.vertices:
            #connecting the two dots
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")


    # def bft(self, starting_node):
    #     visited = []
    #     # create an empty queue
    #     q = Queue()
    #     # Put starting vert in the queue
    #     q.enqueue(starting_node)
    #     while q.size() > 0:
    #         dequeued = q.dequeue()
    #         visited.append(dequeued)
    #         print(dequeued)
    #         for edge in self.vertices[dequeued].edges:
    #             if edge not in visited:
    #                 q.enqueue(edge)
    #     return visited

def bfs(self, starting_node, target_value):
        """
        starting_node: string
        target_value: string
        """
        q = Queue()
        visited = []
        print('===starting node:', starting_node, 'target_value:', target_value)
        q.enqueue(starting_node)

        while q.get_size() > 0:
            current_vert = q.dequeue()
            print('===current_vert:', current_vert)
            if current_vert == target_value:
                return True
            visited.append(current_vert)
            for vert in self.vertices[current_vert].edges:
                if vert not in visited:
                    q.enqueue(vert)
        
        return False



    def dfs(self, starting_node, target_node, visited=None):
        """Depth first traversal using recursion"""
        #Mark the node as visited
        #first pass set to =None
        if visited is None:
            # then create visited = queue
            visited = []
        visited.append(starting_node)
        if starting_node == target_node:
            return True
        # For each child
        for node in self.vertices[starting_node].edges: # .edges is auto: children nodes
            # if that child hasn't been visited
            if node not in visited:
                # call dft() on that
                self.dfs(node, visited)
        return visited





graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.dfs('0', '1')
print(graph.vertices)