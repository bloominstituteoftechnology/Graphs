import random
"""
Simple graph implementation compatible with BokehGraph class.
"""
class Node:
    def __init__(self):
        self.neighbors = []
    def addNeighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node)
    def getNeighbors(self):
        return self.neighbors
    def isNeighbor(self, node):
        return node in self.neighbors

# Another, not-so intuitive solution
# class Vertex:
#     def __init__(self, label, component=-1):
#         self.label = str(label)
#         self.component = component
#
#     def __repr__(self):
#         return 'Vertex: ' + self.label

class Vertex:
    def __init__(self, vertex_id, x=None, y=None, value=None, color=None):
        self.id = int(vertex_id)
        self.x = x
        self.y = y
        self.value = value
        self.color = color
        self.edges = set()
        if self.x is None:
            self.x = 2 * (self.id // 3) + self.id / 10 * (self.id % 3) #So that vertices will not render in a straight line
        if self.y is None:
            self.y = 2 * (self.id % 3) + self.id / 10 * (self.id // 3) #So that vertices will not render in a straight line
        if self.value is None:
            self.value = self.id
        if self.color is None:
            hexValues = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
            colorString = "#"
            for i in range(0, 3):
                colorString += hexValues[random.randint(0,len(hexValues) - 1)]
            self.color = colorString

    # def __repr__(self):
    #     return 'Vertex, id:{} value: {}, connections: {}'.format(self.id, self.value, self.edges)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        # self.components = 0

    def add_vertex(self, vertex_id, value=None): #come back and add code for values...
        if vertex_id in self.vertices:
            raise Exception('Error: adding vertex that already exists')
        #if not set(edges).issubset(self.vertices):
        #    raise Exception('Error: cannot set edges to non-existent vertices')
        self.vertices[vertex_id] = Vertex(vertex_id, value=value) #...here...from five lines up

    def add_edge(self, vertex_1, vertex_2, bidirectional=True):
        if vertex_1 not in self.vertices or vertex_2 not in self.vertices:
            raise IndexError('Error: Verticies to connect not in graph')
        self.vertices[vertex_1].edges.add(vertex_2)
        if bidirectional:
            self.vertices[vertex_2].edges.add(vertex_1)

    def search(self, start, target=None, method='dfs'):
        """Search the graph using BFS or DFS"""
        chosen_data_structure = [start]
        pop_index = 0 if method == 'bfs' else -1
        visited = set([start])

        while chosen_data_structure:
            current = chosen_data_structure.pop(pop_index)
            if current == target:
                break
            visited.add(current)

            chosen_data_structure.extend(self.vertices[current] - visited)
            visited.update(self.vertices[current])

        return visited

graph = Graph()
print(graph.vertices)
graph.add_vertex(1, value="T'Challa!")
graph.add_vertex(2, value="Captain America")
graph.add_edge(1, 2)
#graph.add_vertex('3')
#graph.add_edge('1', '3')
#graph.add_edge('2','3', False)
graph.add_vertex(3)
for vertex, vertex_info in graph.vertices.items():
    print(vertex, "space", vertex_info.value, "space", vertex_info.edges)

#print(graph.search('1', method='bfs'))
