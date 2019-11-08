from util import Queue

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = {}

    def add_edge(self, v1, v2, direction):
        """
        Add a bi-directional edge to the graph.
        """
        opposite_direction = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].update({v2 : direction})
            self.vertices[v2].update({v1 : opposite_direction[direction]})
        else:
            raise IndexError('Vertex does not exist')

    def bfs(self, starting_vertex, passed_visited):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        initial_path = [starting_vertex]
        q.enqueue(initial_path)
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            last_vert = path[-1]
            # If that vertex has not been visited...
            if last_vert not in visited:
                # Mark it as visited...
                visited.add(last_vert)
                # Then add A PATH TO its neighbors to the back of the 
                for v in self.vertices[last_vert]:
                    # print(f'v in bfs: {v}')
                    if v not in passed_visited:
                        path_copy = path[1:]
                        # path_copy.append(v)
                        return path_copy
                    else:
                        # COPY THE PATH
                        path_copy = path[:]
                        # APPEND THE NEIGHOR TO THE BACK
                        path_copy.append(v)
                        q.enqueue(path_copy)