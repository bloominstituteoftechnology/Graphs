"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.graph = {}
    
    def get_vertices(self):
        return [int(k) for k in self.graph]
        
    def add_vertex(self, vertex):
        if vertex not in self.graph: 
            self.graph[vertex] = {}
    
    def add_edge(self, vertex, edge):
        if edge in self.graph:
            if self.graph[vertex] == {}:
                self.graph[vertex] = {edge}

            temp = []

            for k in self.graph[vertex]:
                temp.append(k)

            temp.append(edge)

            self.graph[vertex].update(temp)
        else:
            print(f"Cannot add edge number {edge}. Corresponding vertex doesn't exst.")

        

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('3', '0')
graph.add_edge('3', '2')


print(graph.graph)
