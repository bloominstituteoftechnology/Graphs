"""
Simple graph implementation compatible with BokehGraph class.
"""
# class Vertex:
#     def __init__(self, vertex_id, value, color="white")
#         self.id=vertex_id
#         self.value=value 
#         self.color=color
#         self.edges=[]

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
        
    def add_edge(self, start, end):
        #if start n self.vertices and end in self.vertices:
            self.vertices[start].add(end)
            self.vertices[end].add(start)
        # else:
        #     raise IndexError("That vertex does not exist!")

        

# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(graph.vertices)

#  {
#     '0': {'1', '3'},
#     '1': {'0'},
#     '2': set(),
#     '3': {'0'}
# }   


# def dft(adjList, node_id):
#     print(node_id)
#     for child_node in adjList[node_id]:
#         if child_node not in 
#         dft(adjList, child_node)