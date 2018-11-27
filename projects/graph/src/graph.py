from queue import Queue
from vertex import Vertex

"""
Simple graph implementation
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, vertex_id1, vertex_id2):
        # if both vertices exist
        if vertex_id1 in self.vertices and vertex_id2 in self.vertices:
            # connect each to the other
            self.vertices[vertex_id1].edges.add(vertex_id2)
            self.vertices[vertex_id2].edges.add(vertex_id1)
        else:
            # if both vertices do not exist, raise an IndexError
            raise IndexError('Nonexistent vertex.')

    def bft(self, start_vertex):
        # create a queue
        queue = Queue()
        # create a visited list
        visited = []
        # put the start vertex in the queue
        queue.enqueue(start_vertex)
        # while queue is not empty...
        while queue.len() > 0:
            # remove vertex from queue
            vertex = queue.dequeue()
            # check if it's visited
            if vertex not in visited:
                # if not, mark vertex as visited
                visited.append(vertex)
                # then put all children in queue
                for child in self.vertices[vertex].edges:
                    queue.enqueue(child)
        return visited

    def dft(self, start_vertex):
        # create a stack (as a list)
        stack = []
        # create a visited list
        visited = []
        # put the start vertex in the stack
        stack.append(start_vertex)
        # while stack is not empty...
        while len(stack) > 0:
            # remove vertex from stack
            vertex = stack.pop()
            # check if it's visited
            if vertex not in visited:
                # if not, mark vertex as visited
                visited.append(vertex)
                # then put all children in stack
                for child in self.vertices[vertex].edges:
                    stack.append(child)
        return visited

    def dft_r(self, start_vertex, visited = []):
        # Mark start_vertex as visited
        visited.append(start_vertex)
        # Then call dft_r on each child
        for child in self.vertices[start_vertex].edges:
            # If the child has not been visited...
            if child not in visited:
                # Recursively visit that child
                self.dft_r(child, visited)
        if start_vertex is visited[0]:
            # Once the initial start_vertex's recursion has finished,
            # the entire graph will have been traversed
            # so return visited to get the entire traversal
            return visited

    def bfs(self, start_vertex, search_vertex):
        # create a queue
        queue = Queue()
        # create a visited list
        visited = []
        # put the start vertex in the queue
        queue.enqueue([start_vertex])
        # while queue is not empty...
        while queue.len() > 0:
            # remove vertex from queue
            vertex_path = queue.dequeue()
            vertex = vertex_path[-1]
            # check if it's visited
            if vertex not in visited:
                # if not, mark vertex as visited
                visited.append(vertex)
                # check if its the vertex you are searching for
                if vertex is search_vertex:
                    # if it is, return the path taken
                    return vertex_path
                # then put all children in queue
                for child in self.vertices[vertex].edges:
                    new_vertex_path = list(vertex_path)
                    new_vertex_path.append(child)
                    queue.enqueue(new_vertex_path)
        return None

    def dfs(self, start_vertex, search_vertex):
        # create a stack (as a list)
        stack = []
        # create a visited list
        visited = []
        # put the start vertex in the stack
        stack.append([start_vertex])
        # while stack is not empty...
        while len(stack) > 0:
            # remove vertex from stack
            vertex_path = stack.pop()
            vertex = vertex_path[-1]
            # check if it's visited
            if vertex not in visited:
                # if not, mark vertex as visited
                visited.append(vertex)
                if vertex is search_vertex:
                    return vertex_path
                # then put all children in stack
                for child in self.vertices[vertex].edges:
                    new_vertex_path = list(vertex_path)
                    new_vertex_path.append(child)
                    stack.append(new_vertex_path)
        return None


# Testing implementation
graph = Graph() # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_edge('0', '1')
graph.add_edge('0', '2')
graph.add_edge('0', '3')
graph.add_edge('2', '3')
graph.add_edge('3', '4')
graph.add_edge('4', '5')
print('Graph:', graph.vertices)
print('BFT:', graph.bft('0'))
print('DFT:', graph.dft('0'))
print('DFT_R:', graph.dft_r('0'))
print('BFS:', graph.bfs('0', '5'))
print('DFS:', graph.dfs('0', '5'))