"""
Simple graph implementation compatible with BokehGraph class.
"""
import random
class Vertex:
    def __init__(self, vertex_id, value=None, x=None , y=None, color=None):
        self.id = int(vertex_id)
        self.value = value 
        self.color = color
        self.x = x
        self.y = y
        self.edges = set()
        if self.x is None:
            self.x = 2 * (self.id // 3) + self.id / 10 * (self.id % 3)
        if self.y is None:
            self.y = 2 * (self.id % 3) + self.id / 10 * (self.id // 3)
        if self.value is None:
            self.value = self.id
        if self.color is None:
            hexValues = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
            colorArray = ["F"]
            for i in range(0, 3):
                colorArray.append(hexValues[random.randint(0,len(hexValues) - 1)])
                random.shuffle(colorArray)
            colorString = "#" +"".join(colorArray)
            self.color = colorString

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)
        
    def add_edge(self, start, end):
        if start in self.vertices and end in self.vertices:
            self.vertices[start].edges.add(end)
            self.vertices[end].edges.add(start)
        else:
            raise IndexError("That vertex does not exist!")

    def add_directed_edge(self, start, end):
        if start in self.vertices and end in self.vertices:
            self.vertices[start].edges.add(end)
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

        

# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(graph.vertices)
# print(graph.bfs_connected_component('3'))
# print(graph.dfs('3'))

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

# graph = Graph()
# graph.add_vertex('A')
# graph.add_vertex('B')
# graph.add_vertex('C')
# graph.add_vertex('D')
# graph.add_vertex('E')
# graph.add_vertex('F')
# graph.add_edge('A', 'B')
# graph.add_edge('A', 'C')
# graph.add_edge('B', 'D')
# graph.add_edge('B', 'E')
# graph.add_edge('C', 'F')
# graph.add_edge('F', 'E')

# print(graph.vertices)
# print(graph.bfs_connected_component('A'))
# print(graph.dfs('A'))

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