"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    # v is the vertex
    def add_vertex(self, v):
        self.vertices[v] = set()
    
    # v1 is vertex1, v2 is vertex2
    def add_edge(self, v1, v2):
        if (v1 and v2) in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        if not v1 in self.vertices:
            print(f'No {v1} vertex, edge was not added.')
        if not v2 in self.vertices:
            print(f'No {v2} vertex, edge was not added.')
            

    # def bfs(self, starting_node):
    #     # create a queue
    #     q = Queue()
    #     visited = set()
    #     # enquue the starting node
    #     q.Enqueue(starting_node)
    #     # while the queue is not empty
    #         # dequeue a node from the queue
    #         # mark it as visited
    #         # enqueue all of its children that have not been visited

    # def dfs(self, starting_node):
    #     # create a stack
    #     s = Stack()
    #     visited = set()
    #     # push the starting node
    #     s.Push(starting_node)
    #     # while the stack is not empty
    #         # pop a node from the stack
    #         # mark it as visited
    #         # push all of its children that have not been visited

    # def dft_recursion(self, starting_node, visited=None):
    #     if visited is None:
    #         visited = set()
    #     #if the node has not been visited 
    #         #mark node as visited
    #         #call dft_recursion on all children 
    #         dft_recursion(child_node, visited)

    # def bfs_search(self, starting_node, target_node):
    #     #create queue
    #     q = Queue()
    #     visited = set()
    #     #enqueue the starting vertex
    #     q.Enqueue(starting_v)
    #     #while the queue is not empty, 
    #         #dequeue a vertex from the queue 
    #         #mark it as visited 
    #         # ---*---- if node == target_node: return true
    #         #enqueue all of it's children that have not been visited 
    #     #return false 

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('0', '4')
print(graph.vertices)

