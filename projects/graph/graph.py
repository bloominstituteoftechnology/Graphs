"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
class GraphNode:
    def __init__(self ,value):
        self.value = value
        self.neighbors = []
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {
            
        }
        
         

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # if vertex_id not in self.vertices:
        #    self.vertices[vertex_id]=set()
        # new_node_row = [0] *(len(self.vertices)+1) 
        
        #Matrix way
        
        # for node in self.vertices:
        #     node.append(0)
        # new_node_row = [0]*(len(self.vertices) +1)
        # self.vertices.add(new_node_row)
    # def delete_edge(self, vertex_id):
        # access the v1 remove v2
        # access v2 remove v1
              
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
    
    def bft(self, starting_vertex):
        q = Queue()
        q.enqueue(starting_vertex)
        #mark visited nodes
        visited = set()
        #until queue is empty
        while q.size() > 0:
            v = q.dequeue() # deQ first node
            if v not in visited:
                print(v)
                visited.add(v) #mark as visited
                for n in  self.get_neighbors(v):
                    q.enqueue(n)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        
        """
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        while stack.size()>0:
            
            current = stack.pop()
            
            if current not in visited:
                print(current)
                visited.add(current)
                
                neighbors = self.get_neighbors(current)
                
                for n in neighbors:
                    stack.push(n)
        
        
         

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        visited = set()
        def dft(vertex):
            if vertex in visited:
                return
            else:
                visited.add(vertex)
                print(vertex)
            for neighbor in self.get_neighbors(vertex):
                dft(neighbor)
        dft(starting_vertex)
            
        
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        #mark visited nodes
        visited = set()
        #until queue is empty
        while q.size() > 0:
            v = q.dequeue() # deQ first node
            if  v not in visited:
                print(v)
                visited.add(v) #mark as visited
                for n in  self.get_neighbors(v):
                    q.enqueue(n)
        
          

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()
        
        s.push([starting_vertex])
        visited.add(starting_vertex)
        while s.size>0:
              v = s.pop()
              k = v[ -1]
              if k == destination_vertex:
                  return v
              if k not in visited:
                  visited.add(k)
                  for n in self.get_neighbors(v):
                      s.push(n)
         

    def dfs_recursive(self, starting_vertex, destination_vertex, checked = set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if destination_vertex in self.vertices[starting_vertex]:
            return [starting_vertex, destination_vertex]
        elif len(self.vertices[starting_vertex]):
            if starting_vertex not in checked:
                checked.add(starting_vertex)
                for node in self.vertices[starting_vertex]:
                    return [starting_vertex] + self.dfs_recursive(node, destination_vertex, checked)
            else:
                return []
        else:
            return [starting_vertex]      
            
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
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
     
    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    print('N', graph.get_neighbors(7))
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
    graph = Graph()  # Instantiate your graph
    # graph.add_vertex(8)
    # graph.add_edge(8,7)
    print ('G',graph.vertices)
     