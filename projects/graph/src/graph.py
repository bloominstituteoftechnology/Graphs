"""
Simple graph implementation
"""
print('\nNEW FILE RUN: graph.py')

class Vertex:
    """Vertices have a label and a set of edges."""
    # pylint: disable=too-few-public-methods
    def __init__(self, label):
        self.label = label  # each vertex has a label
        self.edges = set()       # each vertex has a set (unordered dictionary) of edges
    
    def __repr__(self):
        return f'{self.label}'

# Queue class for BFT
class Queue:
  def __init__(self):
    self.size = 0         # not sure if I need this
    self.storage = []

  def enqueue(self, item):
    self.storage.append(item)
    print(f'{item} added to q')
  
  def dequeue(self):
    if len(self.storage) == 0:
      return None
    else:
      return self.storage.pop(0)

  def len(self):
    if len(self.storage) == 0:
      return 0
    else:
      return len(self.storage)

# Stack class for DFT
class Stack:
    def __init__(self):
        self.size = 0      # not sure if I need this
        self.storage = []

    def push(self, item):
        self.storage.append(item)
        print(f'{item} added to s')

    def pop(self):
        if len(self.storage) == 0:
            return None
        else:
            return self.storage.pop(-1)

    def len(self):
        if len(self.storage) == 0:
            return 0
        else:
            return len(self.storage)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # Create empty dict of vertices
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
    
    def bft(self, start_node):
        print('\n--- NEW BFT ---')
        # create a queue:
        q = Queue()
        # make visited a set
        visited = set()
        # make a visited list for printing in order of visitation
        visited_list = []
        # print('Initial visited list: ', visited)
        # put the start node in the queue:
        q.enqueue(start_node)
        # while queue is not empty:
        while q.len() > 0:
            # remove node from queue and return removed node:
            node = q.dequeue()
            # print('Current node: ', node)
            # check if node has been visited:
            if node not in visited:
                # print('node not visited')
                # mark node as visited:
                visited.add(node)
                visited_list.append(node)
                # put all children of node in queue:
                for child in self.vertices[node].edges:
                    q.enqueue(child)  

        print('Final visited list: ', visited_list)

    def dft(self, start_node):
        print('\n--- NEW DFT ---')
        # create empty stack
        s = Stack()
        # create empty visited list
        visited = set()
        # make a visited list for printing in order of visitation
        visited_list = []
        # add start node to the stack
        s.push(start_node)
        # while stack is not empty:
        while s.len() > 0:
            # remove first node from stack and return removed node
            node = s.pop()
            # if node has not been visited:
            if node not in visited:
                # print(f'node {node} not visited')
                visited.add(node)
                visited_list.append(node)
                for child in self.vertices[node].edges:
                    s.push(child)

        print('Final visited list: ', visited_list)
    
    def dft_r(self, start_node, visited = set(), visited_list = []):
        print('\n--- NEW DFT Recursive ---')
        if start_node not in visited:
            visited.add(start_node)
            visited_list.append(start_node)
        for child in self.vertices[start_node].edges:
            if child not in visited:
                self.dft_r(child, visited, visited_list)
        print('final visited set: ', visited)
        print('final visited list: ', visited_list)
    
    def bfs(self, start_node, end_node):
        print('\n--- NEW BFS ---')
        q = Queue()
        visited = set()
        visited_list = []
        q.enqueue(start_node)

        while q.len() > 0:
            node = q.dequeue()
            if node not in visited:
                visited.add(node)
                visited_list.append(node)
                if end_node == node:
                    print(f'node {end_node} reached')
                    print(f'path: ', visited_list)
                    return True
                
                for child in self.vertices[node].edges:
                    q.enqueue(child)
        return False
        
    def dfs(self, start_node, end_node):
        print('\n--- NEW DFS ---')
        s = Stack()
        visited = set()
        visited_list = []
        s.push(start_node)

        while s.len() > 0:
            node = s.pop()
            if node not in visited:
                visited.add(node)
                visited_list.append(node)
                if end_node == node:
                    print(f'node {end_node} reached')
                    print(f'path: ', visited_list)
                    return True
                for child in self.vertices[node].edges:
                    s.push(child)


graph = Graph()     # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# graph.add_edge('1', '2')
# graph.add_edge('0', '4')
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_edge(0, 1)
graph.add_edge(0, 3)
graph.add_edge(1, 2)
graph.add_edge(0, 4)
print('Number of vertices in graph: ', len(graph.vertices))
print('Vertices: ', graph.vertices)
graph.bft(1)
graph.dft(1)
graph.dft_r(1)
graph.bfs(0, 3)
graph.dfs(0, 3)