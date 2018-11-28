"""
Simple graph implementation compatible with BokehGraph class.
"""

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    def enqueue(self, item):
        self.storage.append(item)
        self.size += 1
    def dequeue(self):
        if self.size:
            self.size-= 1
        return self.storage.pop(0)
    def len(self):
        return self.size

class Stack:
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

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices={}
    def add_vertex(self,vertex_id):
        self.vertices[vertex_id]=Vertex(vertex_id)
    def add_edge(self,v1,v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError('That vertex does not exist.')

    def bft(self, start_vertex):
        queue = Queue()
        visited = []
        queue.enqueue(start_vertex) 
        while queue.len() > 0:
            vertex = queue.dequeue()
            if vertex not in visited:            
                visited.append(vertex)
                for child in self.vertices[vertex].edges:
                    queue.enqueue(child)
        return visited

    def bfs(self, start_vertex, search_vertex):
        queue = Queue()
        visited = []
        queue.enqueue(start_vertex) 
        while queue.len() > 0:
            vertex_path = queue.dequeue()
            vertex = vertex_path[-1]
            if vertex not in visited:            
                visited.append(vertex)
                if vertex is search_vertex:
                    return vertex_path
                for child in self.vertices[vertex].edges:
                    new_vertex_path = list(vertex_path)
                    new_vertex_path.append(child)
                    queue.enqueue(new_vertex_path)
        return None


    def dft(self, start_vertex):
        stack = []
        visited = []
        stack.append(start_vertex)
        while len(stack) > 0:    
            vertex = stack.pop()  
            if vertex not in visited:       
                visited.append(vertex)   
                for child in self.vertices[vertex].edges:
                    stack.append(child)
        return visited

    def dfs(self, start_vertex, search_vertex):
        stack = []
        visited = []
        stack.append(start_vertex)
        while len(stack) > 0: 
            vertex_path = stack.pop()   
            vertex = vertex_path[-1] 
            if vertex not in visited:       
                visited.append(vertex)   
                if vertex is search_vertex:
                    return vertex_path
                for child in self.vertices[vertex].edges:
                    new_vertex_path = list(vertex_path)
                    new_vertex_path.append(child)
                    stack.append(new_vertex_path)
        return None
    
    def dft_r(self, start_vertex, visited = []):
        visited.append(start_vertex)
        for child in self.vertices[start_vertex].edges: 
            if child not in visited:      
                self.dft_r(child, visited)
            if start_vertex is visited[0]:                  
                return visited

class Vertex:
    def __init__(self,value):
        self.value = value 
        self.edges = set()


  
  
graph = Graph()  
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('0', '2')
graph.add_edge('1', '4')
graph.add_edge('2', '4')
graph.add_edge('3', '4')
print(graph.vertices)
print('BFS:', graph.bfs('0', '3'))
print('BFT:', graph.bft('0'))
print('DFT:', graph.dft('0'))
print('DFS:', graph.dfs('0', '3'))
print('DFT_R:', graph.dft_r('0'))