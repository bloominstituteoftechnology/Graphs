# parent child relationship

class Stack():
    def __init__(self):
        self.stack = []
    def __repr__(self):
        return str(self.stack)

    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def __repr__(self):
        return str(self.vertices)

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()
        while stack.size() > 0:
            currrent_path = stack.pop()
            print(f'\nthe currrent_path is {currrent_path}')
            current_node = currrent_path[- 1]
            print(f'\nthe current_node is {current_node}')
            if current_node == destination_vertex:
                return currrent_path
            if current_node not in visited:
                    visited.add(current_node)
                    print(f'visted: {visited}')
                    for neighbor in self.get_neighbors(current_node):
                        newPath = list(currrent_path)
                        newPath.append(neighbor)
                        print(f'the new path is: {newPath}')
                        stack.push(newPath)

    def dft(self, starting_vertex):
            """
            Print each vertex in depth-first order
            beginning from starting_vertex.
            """

            stack = Stack()
            visited = set()
            stack.push(starting_vertex)
            print(f'the stack is: {stack}')
            while stack.size() > 0:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    for child in self.get_neighbors(node):
                        print(f'child of {node} is {child}')
                        stack.push(child)
            return node

    def earliest_ancestor(self, starting_node):
        # use DFS to get the fartherst distance
        search = self.dft(starting_node)
        return search

graph = Graph()

graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_vertex(7)
graph.add_vertex(8)
graph.add_vertex(9)
graph.add_vertex(10)
graph.add_vertex(11)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(3, 6)
graph.add_edge(4, 5)
graph.add_edge(4, 8)
graph.add_edge(5, 6)
graph.add_edge(5, 7)
graph.add_edge(1, 2)
graph.add_edge(2, 4)
graph.add_edge(8, 9)
graph.add_edge(10, 1)
graph.add_edge(11, 8)

print(graph)

print(graph.earliest_ancestor(1))