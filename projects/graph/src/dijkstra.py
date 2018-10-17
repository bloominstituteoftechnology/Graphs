from heapq import *

class WeightedGraph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        if value in self.vertices:
            raise Exception('That vertex already exists.')
        else:
            self.vertices[value] = set()

    def add_edge(self, v1, v2, weight):
        if v1 not in self.vertices or v2 not in self.vertices:
            raise Exception('Invalid vertex: one or more of the vertices provided is invalid.')
        else:
            self.vertices[v1].add((weight, v2))

    def dijkstra(self, start, finish):
        """
        :param start: str of vertex name
        :param finish: str of vertex name
        :return: tuple, (distance, [path])
        This is an implementation of Dijkstra's algorithm by utilizing a priority queue. I used Python's built in
        heapq library to implement a simple priority queue, and used BFS to look for the shortest path from the
        start vertex to the finish.
        """
        q = [(0, start, [])]
        visited = set()
        min_dist = {start: 0}
        while q:
            cost, vtx, path = heappop(q)
            if vtx not in visited:
                visited.add(vtx)
                # path is constructed from start to finish
                path = path + [vtx]
                if vtx == finish:
                    return cost, path

                for curr_cost, vtx2 in self.vertices.get(vtx, ()):
                    # looks through the connected vertices
                    if vtx2 in visited:
                        # if vertex is visited, we don't need to do anything
                        continue
                    prev = min_dist.get(vtx2, None)
                    updated_cost = cost + curr_cost
                    if prev is None or updated_cost < prev:
                        # only updates if the cost/distance is lower, otherwise doesn't add to our priority queue
                        min_dist[vtx2] = updated_cost
                        heappush(q, (updated_cost, vtx2, path))
        return None


graph = WeightedGraph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1', 3)
graph.add_edge('0', '2', 5)
graph.add_edge('1', '3', 7)
graph.add_edge('2', '3', 1)

print(graph.dijkstra('0', '3'))
