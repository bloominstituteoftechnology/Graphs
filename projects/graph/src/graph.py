"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, vertex_id, value, x=None , y=None, color="white"):
        self.id = int(vertex_id)
        self.value = value 
        self.color = color
        self.x = x
        self.y = y
        self.edges
        if self.x is None:
            self.x = self.id
        if self.y is None:
            self.y = self.id
        if self.value is None:
            self.value = self.id

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
        
    def add_edge(self, start, end):
        if start in self.vertices and end in self.vertices:
            self.vertices[start].add(end)
            self.vertices[end].add(start)
        else:
            raise IndexError("That vertex does not exist!")
    
    def bfs_connected_component(self, start):
        explored = []
        queue = [start]

        while queue:
            vertex = queue.pop(0)
            if vertex not in explored:
                explored.append(vertex)
                neighbours = graph.vertices[vertex]
                for neighbour in neighbours:
                    queue.append(neighbour)
        return explored

    def dfs(self, start):
        stack = []
        stack.append(start)
        visited = set()
        while stack:
            current_vertex = stack.pop()
            visited.add(current_vertex)     
            stack.extend(self.vertices[current_vertex] - visited)
        return visited

        

#graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
#print(graph.vertices)
#print(bfs_connected_component(graph, '3'))

# graph = Graph()  # Instantiate your graph
# graph.add_vertex('A')
# graph.add_vertex('B')
# graph.add_vertex('C')
# graph.add_vertex('D')
# graph.add_vertex('E')
# graph.add_vertex('F')
# graph.add_vertex('G')
# graph.add_edge('A', 'B')
# graph.add_edge('A', 'C')
# graph.add_edge('A', 'E')
# graph.add_edge('B', 'D')
# graph.add_edge('B', 'E')
# graph.add_edge('C', 'F')
# graph.add_edge('C', 'G')
# graph.add_edge('D', 'E')

graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'F')
graph.add_edge('F', 'E')

print(graph.vertices)
print(graph.bfs_connected_component('A'))
print(graph.dfs('A'))

# {
#     '0': {'1', '3'},
#     '1': {'0'},
#     '2': set(),
#     '3': {'0'}
#  }   


# def dft(adjList, node_id):
#     print(node_id)
#     for child_node in adjList[node_id]:
#         if child_node not in 
#         dft(adjList, child_node)