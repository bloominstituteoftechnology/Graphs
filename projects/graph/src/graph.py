"""
Simple graph implementation compatible with BokehGraph class.
"""
import sys


class Vertex:
    """Represent a vertex with an id, value=None, color, edges"""

    def __init__(self, vertex_id, value=None, color="red"):
        self.vertex_id = str(vertex_id)
        self.value = value
        self.color = color
        self.edges = set()

        if self.value is None:
            self.value = self.vertex_id

    def __repr__(self):
        return 'Vertex: ' + self.vertex_id


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = Vertex(vertex)
        else:
            sys.exit("Vertex {} already exists.".format(vertex))

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.vertices:
            sys.exit("No '{}' vertex!".format(vertex1))
        elif vertex2 not in self.vertices:
            sys.exit("No '{}' vertex!".format(vertex2))
        else:
            self.vertices[vertex1].edges.add(vertex2)
            self.vertices[vertex2].edges.add(vertex1)

    def Search(self, start, target=None, type="bfs"):
        """Search the graph using BFS/DFS based on type"""
        queue = [start]
        # remove first if a bfs (queue) and last if dfs (stack)
        remove_index = 0 if type == "bfs" else -1
        # set up our visited list
        visited = []

        while queue:
            # get first/last item
            vert = queue.pop(remove_index)
            if vert not in visited:
                if self.vertices[vert].value == target:
                    return True
                # add to visited
                visited.append(vert)
                # set up to visit all the children
                for child in self.vertices[vert].edges:
                    queue.append(child)
        return False

    def Shortest(self, vertex_id, target):
        queue = []
        #  add the current vert to cue
        queue.append([vertex_id])
        visited = []
        while len(queue):
            # get first element
            path = queue.pop(0)
            # get last element
            vert = path[-1]
            if vert not in visited:
                if self.vertices[vert].value == target:
                    return path
                visited.append(vert)
                for next_vert in self.vertices[vert].edges:
                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.append(new_path)
        return None


# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# # print(graph.vertices)
# print(graph.Search('0', '0', 'bfs'))
# print(graph.Search('0', '3', 'dfs'))
# print(graph.Shortest('0', '1'))
