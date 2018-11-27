"""
Simple graph implementation compatible with BokehGraph class.
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

class Queue:
  def __init__(self):
    self.size = 0
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

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # Start here:
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
    
    def bfs(self, start_node):
        print('\n--- NEW BFS ---')

        # create a queue:
        q = Queue()

        # create visited list, False at each index, number of indices = (number of vertices in graph):
        visited = [False] * (len(self.vertices))
        # visited = []
        # print('Initial visited list: ', visited)

        # put the start node in the queue:
        q.enqueue(start_node)

        # while queue is not empty:
        while q.len() > 0:
            # remove node from queue and return removed node:
            node = q.dequeue()
            print('Current node: ', node)

            if node == 0:
                pass
            # check if node has been visited:
            if node not in visited:
                print('node not in visited')
                # mark node as visited:
                visited[node] = True
                # print('Visited list with new node: ', visited)
                # put all children of node in queue:
                for child in self.vertices[node].edges:
                    q.enqueue(child)
                    # mark node as visited:
                    visited[child] = True
                    return self.bfs(child)

        print('Final visited list: ', visited)



graph = Graph()  # Instantiate your graph
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
graph.bfs(1)
