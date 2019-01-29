"""
Simple graph implementation
"""

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Vertex:
	def __init__(self, vertex_id):
		self.vertex_id = vertex_id
		self.edges = set()
	def __repr__(self):
		return f'{self.edges}'


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        

    def add_vertex(self,key):
        self.vertices[key] = Vertex(key) 


    def add_edge(self,ver1,ver2):
        if ver1 in self.vertices and ver2 in self.vertices:
            self.vertices[ver1].edges.add(ver2)
            self.vertices[ver2].edges.add(ver1)
        else:
            raise IndexError("That vertex does not exist")

    

    def bft(self, starting_node):
        
        storage = Queue()
        visited = set()
        storage.enqueue(starting_node)

        while storage.size() > 0:
            node = storage.dequeue()
            if node not in visited:
                print(node)
                visited.add(node)
                for next_node in self.vertices[node].edges:
                    storage.enqueue(next_node)
        return visited


    def dft(self, starting_node):

        visited = set()
        storage = Stack()
        storage.push(starting_node)

        while storage.size() > 0:
            node = storage.pop()
            if node not in visited:
                print(node)
                visited.add(node)
                for next_node in self.vertices[node].edges:
                    storage.push(next_node)
        return visited

    def dft_r(self, starting_node, visited=None):
        if visited is None:
            visited =set()
        visited.add(starting_node)
        print(starting_node)
        for child_node in self.vertices[starting_node].edges:
            if child_node not in visited:
                self.dft_r(child_node, visited)
    


    def bfs(self, starting_node, target_node):
        storage = Queue()
        visited = []
        storage.enqueue([starting_node])
        while storage.size() > 0:
            path = storage.dequeue()
            vertex = path[-1]
            if vertex not in visited:
                visited.append(vertex)
                if vertex is target_node:
                    return path
                for child in self.vertices[vertex].edges:
                    new_path = list(path)
                    new_path.append(child)
                    storage.enqueue(new_path)
        return None

    def dfs(self, starting_node, target_node):
        storage = Stack()
        visited = []
        storage.push([starting_node])
        while storage.size() > 0:
            path = storage.pop()
            vertex = path[-1]
            if vertex not in visited:
                visited.append(vertex)
                if vertex is target_node:
                    return path
                for child in self.vertices[vertex].edges:
                    new_path = list(path)
                    new_path.append(child)
                    storage.push(new_path)
        return None

    # def bfs_path(self, starting_node, target_node):
    #     storage = Queue()
    #     visited = set()
    #     storage.enqueue(starting_node)

    #     while storage.size() > 0:
    #         #Dequeue a path from the queue
    #         path = storage.dequeue()
    #         node = path[-1]

    #         if node not in visited:
    #             if node == target_node:
    #                 return path
               


    #             for next_node in self.vertices[node]:
    #                 storage.enqueue(next_node)
    #     return False



        # q = [[1,2,3] [1,2,4]]
        #visited = {1,2,3}
