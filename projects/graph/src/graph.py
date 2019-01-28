"""
Simple graph implementation
"""
"""
{
'0': {'1', '3'},
'1': {'0'},
'2': {set()},
'3': {'0'}
}
"""
import pprint
import queue

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, destination = None, label = None):
        self.vertices = {}
        self.edges = set()
        self.destination = destination
        self.label = label



    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
        print(self.vertices)

    def add_edge(self, vertex_start, vertex_end):
        if vertex_start not in self.vertices:
            print(f'You chose: {vertex_start}. That Beginning Vertex does not exist...')
            return
        if vertex_end not in self.vertices:
            print(f"You chose: {vertex_end} That End Vertex does not exist...")
            return
        for i in self.vertices:
            # temp = set()
            # temp.add(i)
            if i == vertex_start:
                self.vertices[vertex_start].add(vertex_end)
                print(self.vertices)
            if vertex_end == i:
                self.vertices[vertex_end].add(vertex_start)
                print(self.vertices)



    def breadth_first_traverse(self, starting_vertex):
        # create a _queue_ FIFO
        q = queue.Queue()
        visited = set()
        # Mark the first node as visited
        # print(starting_vertex)
        # visited.add(starting_vertex)
        # Enqueue the starting vertex
        q.Enqueue(starting_vertex)
        # while the queue is not empty 
            # dequeue a node from the queue
            # Mark it as visited
            # Enqueue all of its children

    def depth_first_traverse(self, starting_vertex):
        # create a stack LIFO
        s = queue.LifoQueue()
        visited = set()
        # visited.add(starting_vertex)
        # Push the starting vertex
        q.Enqueue(starting_vertex)
        # while the stack is not empty
            # pop a node from the queue
            # Mark it as visited
            # push all of its children

    def dfr_r(self, starting_vertex, visited=None):
        if visited is None:
            visited = set()
        #mark the node as visited
        #call dft_r on all children
        dft_r(child_vertex, visited)


    def breadth_first_traverse(self, starting_vertex):
        # create a _queue_ FIFO
        q = Queue()
        visited = set()
        # Mark the first node as visited
        # print(starting_vertex)
        # visited.add(starting_vertex)
        # Enqueue the starting vertex
        q.Enqueue(starting_vertex)
        # while the queue is not empty
            # dequeue a node from the queue
            # Mark it as visited
            # If node == target node: return True
            # Enqueue all of its children
        # return False


def print_vertex():
    graph = Graph()
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    graph.add_edge('6', '7')
    print("The Vertices: ",graph.vertices)
print_vertex()
