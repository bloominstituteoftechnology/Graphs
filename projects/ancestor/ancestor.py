from util import Queue

class Graph: 
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add[v2]
        else:
            raise IndexError("vertex does not exist")


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bfs(self, starting_vertex, destination_vertex)
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()
        while queue.size() > 0:
            path = queue.dequeue()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for next_vert in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.enqueue(new_path)

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for el in ancestors:
        graph.add_vertex(el)

    

