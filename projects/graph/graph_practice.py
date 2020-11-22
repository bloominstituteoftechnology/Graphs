from util import Stack, Queue


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vertex1, vertex2):
        self.vertices[vertex1].add(vertex2)

    def find_neighbors(self, vertex):
        return self.vertices[vertex]

    def bft(self, start_vertex, visited=[]):
        q = Queue()

        q.enqueue(start_vertex)

        while q.size() > 0:
            vertex = q.dequeue()
            if vertex not in visited:
                visited.append(vertex)
                print(vertex)
            else:
                break
            for neighbor in self.find_neighbors(vertex):
                q.enqueue(neighbor)

    def dft(self, start_vertex, visited=[]):
        s = Stack()
        s.push(start_vertex)

        while s.size() > 0:
            vertex = s.pop()
            if vertex not in visited:
                visited.append(vertex)
                print(vertex)
            else:
                break
            for neighbor in self.find_neighbors(vertex):
                s.push(neighbor)

    def bfs(self, start_vertex, target_vertex, visited=[]):
        q = Queue()

        q.enqueue([start_vertex])

        while q.size() > 0:
            new_path = q.dequeue()
            vertex = new_path[-1]
            if vertex not in visited:
                if vertex == target_vertex:
                    print(new_path)
                    return new_path
                else:
                    visited.append(vertex)

            for neighbor in self.find_neighbors(vertex):
                pathy = new_path + [neighbor]
                q.enqueue(pathy)

    def dfs(self, start_vertex, target_vertex, visited=[]):
        s = Stack()

        s.push([start_vertex])

        while s.size() > 0:
            new_path = s.pop()
            vertex = new_path[-1]
            if vertex not in visited:
                if vertex == target_vertex:
                    print(new_path)
                    return new_path
                else:
                    visited.append(vertex)

            for neighbor in self.find_neighbors(vertex):
                pathy = new_path + [neighbor]
                s.push(pathy)

    def dfs_recurse(self, start_vertex, target_vertex, visited=None, path=None):
        if visited is None:
            visited = set()
        if path == None:
            path = []
        visited.add(start_vertex)

        path = path + [start_vertex]

        if start_vertex == target_vertex:
            return path

        for neighbor in self.find_neighbors(start_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recurse(
                    neighbor, target_vertex, visited, path)

                if new_path is not None:
                    return new_path

        return None


graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_vertex(7)
graph.add_edge(5, 3)
graph.add_edge(6, 3)
graph.add_edge(7, 1)
graph.add_edge(4, 7)
graph.add_edge(1, 2)
graph.add_edge(7, 6)
graph.add_edge(2, 4)
graph.add_edge(3, 5)
graph.add_edge(2, 3)
graph.add_edge(4, 6)

print(graph.vertices)
# graph.bft(1)
# graph.dft(1)

# print(graph.bfs(1, 6))
print(graph.dfs_recurse(1, 6))

# graph.dft(1)

# g = Graph()
# g.add_vertex(5)
# g.add_vertex(10)
# g.add_vertex(8)
# g.add_vertex(3)
# g.add_vertex(4)
# g.add_vertex(7)
# g.add_vertex(6)
# g.add_vertex(9)


# g.add_edge(5, 8)
# g.add_edge(5, 10)
# g.add_edge(10, 6)
# g.add_edge(10, 3)
# g.add_edge(8, 3)
# g.add_edge(3, 7)
# g.add_edge(3, 4)
# g.add_edge(4, 9)

# # g.bft(5)
# # g.dft(5)
# # g.bfs(5, 9)
# g.dfs(5, 9)
