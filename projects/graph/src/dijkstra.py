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
        q = [(0, start, [])]
        visited = set()
        min_dist = {start: 0}
        while q:
            cost, vtx, path = heappop(q)
            if vtx not in visited:
                visited.add(vtx)
                path = path + [vtx]
                if vtx == finish:
                    return (cost, path)

                for curr_cost, vtx2 in self.vertices.get(vtx, ()):
                    if vtx2 in visited:
                        continue
                    prev = min_dist.get(vtx2, None)
                    updated_cost = cost + curr_cost
                    if prev is None or updated_cost < prev:
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

print(graph.vertices)

print(graph.dijkstra('0', '3'))