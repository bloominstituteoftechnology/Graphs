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
from queue import *


class Vertex:
    def __init__(self, name, neighbors=list(), distance=9999, color='black'):
        self.name = name #label
        self.neighbor = list() #same as edges?
        self.distance = 9999 #destination
        self.color = 'black' #black for visited, red for not visited



class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.edges = set()
        # self.destination = destination
        # self.label = label



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
        q = []
        visited = set()
        # Enqueue the starting vertex
        q.append(starting_vertex)
        print(q)
        # while the queue is not empty
        while len(q) > 0:
            # dequeue a node from the queue
            deq = q.pop()

            # Mark it as visited
            visited.add(deq)
            print("visited: ",visited)
            # Enqueue all of its children
            for i in self.vertices[deq]:
                if i not in visited:
                    q.append(i)
                if len(q) == 0:
                    return visited


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

    def dfr_2(self, v, visited, storage):

        for key in self.vertices:
            list_of_keys = [key]

            if key == v:

                visited[list_of_keys.index(v)] = True
                storage.insert(0, v)
                print("visited recursively: ",storage)

        for i in self.vertices[v]:
            ano_list = [x for x in self.vertices]
            if visited[ano_list.index(i)] == False:
                print(visited)
                self.dfr_2(i, visited, storage)


    def dfr_r(self, starting_vertex):
        visited_nodes = []
        visited = [False]*(len(self.vertices))
        print(visited)
        #mark the node as visited
        #call dft_r on all children
        self.dfr_2(starting_vertex, visited, visited_nodes)


    # def breadth_first_traverse(self, starting_vertex):
    #     # create a _queue_ FIFO
    #     q = Queue()
    #     visited = set()
    #     # Mark the first node as visited
    #     # print(starting_vertex)
    #     # visited.add(starting_vertex)
    #     # Enqueue the starting vertex
    #     q.Enqueue(starting_vertex)
    #     # while the queue is not empty
    #         # dequeue a node from the queue
    #         # Mark it as visited
    #         # If node == target node: return True
    #         # Enqueue all of its children
    #     # return False


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
    for v in graph.vertices['0']:
        print(v)
    print(graph.breadth_first_traverse('0'))
    print(graph.dfr_r('0'))

print_vertex()
