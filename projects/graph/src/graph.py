"""
Simple graph implementation
"""
from structures import Queue
# from structures import LinkedList


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, v):
        if v is not None:
            self.vertices[v] = set()
        else:
            return "Error: Vertex can not be none"

    def add_edge(self, vertex1, vertex2):
        if vertex1 and vertex2:
            self.vertices[vertex1].add(vertex2)

    def bft(self, starting_point):
        q = Queue()
        visited = []
        q.enqueue(starting_point)
        while q.len() is not 0:
            n = q.dequeue()
            if n not in visited:
                visited.append(n)
                # print(visited)
                for i in self.vertices[f"{n}"]:
                    q.enqueue(f"{i}")
        return visited

    # Using Recursion
    def dft(self, starting_point, next_set=[], visited=[]):
        visited.append(starting_point)
        for num in self.vertices[f"{starting_point}"]:
            next_set.append(num)
        for node in next_set:
            print(node)
            visited.append(node)
            if node not in visited:
                self.dft(next_set[0], next_set)

    # Using a stack
    def dfts(self, starting_point):
        # Pseudo code
        # ---------------------------------------------
        # Create a stack
        visited = []
        stack = []
        # add starting_point to that stack
        stack.append(starting_point)
        # while the stack is not None:
        while len(stack) > 0:
            # take the first node in stack out
            visited.append(stack.pop(0))
            # put it in a visited array
            # if child(ren) is not in the visited array
            for node in self.vertices[f"{visited[len(visited)-1]}"]:
                if node not in visited:
                    stack.append(node)
                    # print("APPENDED NODE L66 : ", node)
                    print(node)
                # Place child(ren) in the stack
        return visited
        # Should work in theory

    def bfs(self, starting_point, value):
        a = self.bft(starting_point)
        print("a=", a)
        if str(value) in a:
            return True
        return False

    def dfs(self, starting_point, value):
        a = self.dfts(starting_point)
        if str(value) in a:
            return True
        return False









