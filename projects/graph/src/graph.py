"""
Simple graph implementation compatible with BokehGraph class.
"""

from random import randint

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, vertices_list={}):
        self.vertices_list = vertices_list

    def show_graph(self):
        print(self.vertices_list)

    def add_vertex(self, vertex):
        self.vertices_list[vertex] = set()

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.vertices_list:
            print(f"⚠️ Vertice {from_vertex} is not in the graph")
            return False
        if to_vertex not in self.vertices_list:
            print(f"⚠️ Vertice {to_vertex} is not in the graph")
            return False
        # if edge already in set
        if to_vertex in self.vertices_list[from_vertex]:
            return False
    
        self.vertices_list[from_vertex].add(to_vertex)
        return True

    def randomise_graph(self, num_vertices, num_edges):
        # v * v edges to fill all vertices 
        # including vertex pointing itself
        if num_edges > num_vertices * num_vertices:
            print(f"⚠️ Number of edges exceeds maximum")

        for vertex in range(0, num_vertices):
            self.add_vertex(str(vertex))

        edge = 0

        # while loop to create new edge
        while edge < num_edges:
            from_vertex = str(randint(0, num_vertices - 1))
            to_vertex = str(randint(0, num_vertices - 1))
            if self.add_edge(from_vertex, to_vertex):
                edge += 1 

        self.show_graph()

graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '2')
# graph.add_edge('2', '3')
graph.randomise_graph(5, 6)