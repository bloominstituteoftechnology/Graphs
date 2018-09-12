"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    # Initialize an empty set when adding a vertex to the graph
    def add_vertex(self,vertex_id, color="white"):
        self.vertices[vertex_id] = set()
    # def get_edges(self,vertex_id):
    #     self.vertices[vertex_id]
    
    # When adding an edge, assume its undirected and check for membership
    def add_edge(self,v1,v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError('That vertex value is not available. please add it first')
    
    # When adding an directed edge, only check source node/vertex for membership
    def add_directed_edge(self,v1,v2):
        if v1 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex value is not available. please add it first')

    # Recursive DFT            
    def dft(self, adjList,vertex_id, visited):
        print(f"DFT Listing: {vertex_id}")
        visited.append(vertex_id)
        for child in adjList[vertex_id]:
            if child not in visited:
                self.dft(adjList,child,visited)

    def dfs(self, adjList,vertex_id, visited, search):
        if vertex_id == search:
            return True
        visited.append(vertex_id)
        for child in adjList[vertex_id]:
            if child not in visited:
                self.dfs(adjList,child,visited, search)
        return False
            
    def bft(self, adjList, vertex_id):
        frontier = []
        frontier.append(vertex_id)
        visited = []
        while len(frontier) > 0:
            n = frontier.pop(0)
            if n not in visited:
                print(f"BFT Listing: {n}")
                visited.append(n)
                for next_vertex in adjList[n]:
                    frontier.append(next_vertex)
# class Vertex:
#     def __init__(self, vertex_id, value, color="white"):
#         self.id = vertex_id
#         self.value = value
#         self.color = color
#         self.edges = []


# Testing
graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_vertex('8')
graph.add_vertex('9')
print(graph.vertices)
graph.add_edge('0', '1')
graph.add_edge('0', '2')
graph.add_edge('0', '3')
graph.add_edge('1', '4')
graph.add_edge('1', '5')
graph.add_edge('2', '6')
graph.add_edge('2', '7')
graph.add_edge('3', '8')
graph.add_edge('3', '9')
print(graph.vertices)
print('\n DFT:')
graph.dft(graph.vertices, '0',[] )
print('\n BFT:')
graph.bft(graph.vertices, '0')
print('\n Search:')
print(graph.dfs(graph.vertices, '0',[], '2'))
