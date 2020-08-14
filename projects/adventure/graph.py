from queue import Queue

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def get_connections(self, room_id):
        queue = Queue()
        visited = {}
        queue.enqueue([room_id])

        while queue.size() > 0:
            path = queue.dequeue()
            last_room = path[-1]

            if last_room not in visited:
                visited[last_room] = path

                for room in self.vertices[last_room]:
                    path_copy = list(path)
                    path_copy.append(room)
                    queue.enqueue(path_copy)

        return visited