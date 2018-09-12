"""
Simple graph implementation compatible with BokehGraph class.
"""
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            raise ValueError(f'Vertex {vertex} already exists')
    
    def add_edge(self, vertex_1, vertex_2):
        if vertex_2 in self.vertices:
            if vertex_1 not in self.vertices[vertex_2]:
                self.vertices[vertex_1].add(vertex_2)
                self.vertices[vertex_2].add(vertex_1)
            else:
                raise ValueError(f'Edge {vertex_1} already exists with Vertex {vertex_2}')
        else:
            raise ValueError(f'Vertex {vertex_2} does not exist')

    def bfs(self, start, target=None):
        visited, queue = set([str(start)]), [str(start)]

        while queue:
            vertex = queue.pop(0)

            if vertex == target:
                break

            print(f'visited: {vertex}')
            visited.add(vertex)
            queue.extend(self.vertices[vertex] - visited)
            visited.update(self.vertices[vertex])
        
        return visited
        
    def dfs(self, start, target=None):
        visited, stack = set([str(start)]), [str(start)]

        while stack:
            vertex = stack.pop()

            if vertex == target:
                break

            print(f'visited: {vertex}')
            visited.add(vertex)
            stack.extend(self.vertices[vertex] - visited)
            visited.update(self.vertices[vertex])

        return visited

    def search(self, method, start, target=None):
        if method == 'dfs':
            return self.dfs(start, target)
        else:
            return self.bfs(start, target)

demo_g = Graph()
demo_g.add_vertex('0')
demo_g.add_vertex('1')
demo_g.add_vertex('2')
demo_g.add_vertex('3')
demo_g.add_edge('0', '1')
demo_g.add_edge('0', '3')
demo_g.add_edge('1', '2')
# for vertex in demo_g.vertices:
#     print(f'{vertex}: {demo_g.vertices[vertex]}')

# print(demo_g.bfs('0'))
# print(demo_g.bfs('1'))
# print(demo_g.bfs('2'))
# print(demo_g.bfs('3'))
# print(demo_g.dfs('0'))
# print(demo_g.dfs('1'))
# print(demo_g.dfs('2'))
# print(demo_g.dfs('3'))

print(demo_g.search(method=None, start='0', target='3'))
print(demo_g.search(method='dfs',start='0',target='3'))