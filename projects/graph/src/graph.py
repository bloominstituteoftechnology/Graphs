"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
    
    def add_edge(self, vert, edge2):
        # specify which vertex
        # receive inputs for edge cases regard that vertex
        # update vertex set values
        # print the dictionary
        #code is below this line
        # vert = f"Please specify vertex: {input()}"
        
        # self.vertices[vert].update(edge) 
        # print(self.vertices)
        if vert not in self.vertices:
            raise Exception(f"No{vert} vertex")
            self.vertices[vert].add(edge2)
            if vert not in self.vertices:
                raise Exception(f"No {edge2} vertex")
            self.vertices[vert].add(edge2)


        self.vertices[vert].add(edge2)
        self.vertices[edge2].add(vert)



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    # graph.add_edge('0', '4')
    # graph.add_edge('3', '0')




    print(graph.vertices)