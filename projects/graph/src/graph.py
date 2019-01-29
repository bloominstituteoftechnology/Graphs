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

    def add_edge_bi(self, vertex_start, vertex_end):
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

    def add_edge_mono(self, vertex_start, vertex_end):
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
        # create a _queue_ FIFO
        stack = []
        visited = set()
        # Enqueue the starting vertex
        stack.append(starting_vertex)
        print(stack)
        # while the queue is not empty
        while len(stack) > 0:
            # dequeue a node from the queue
            deq = stack.pop(0)

            # Mark it as visited
            visited.add(deq)
            print("visited: ",visited)
            # Enqueue all of its children
            for i in self.vertices[deq]:
                if i not in visited:
                    stack.append(i)
                if len(stack) == 0:
                    return visited

    def dfr_2(self, v, visited, storage):

        for key in self.vertices:
            list_of_keys = [key]

            if key == v:
                print(v)
                visited[list_of_keys.index(v)] = True
                storage.insert(-1, v)
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

    def dft_recurse(self, starting_vertex, visited = None):
        if visited == None:
            visited = set()

        visited.add(starting_vertex)
        print(starting_vertex)
        for i in self.vertices[starting_vertex]:
            if i not in visited:
                self.dft_recurse(i, visited)
                print("Visited 2nd Recurse Func: ",visited)


    def breadth_first_search(self, starting_vertex, target):
        # create a _queue_ FIFO
        q = []
        visited = []
        # Enqueue the starting vertex
        q.append(starting_vertex)
        print("stack: ",q)
        # while the queue is not empty
        while len(q) > 0:
            # dequeue a node from the queue
            path = q.pop()
            node = path[-1]
            if node not in visited:
                # Mark it as visited
                visited.append(node)
                print("visited breadth: ",visited)
                if target in visited:
                    print("Path: ",path)
                    print("Dup_Path: ", dup_path)
                    return dup_path
                # Enqueue all of its children
                for i in self.vertices[node]:
                    if i not in visited:
                        dup_path = list(path)
                        dup_path.append(i)
                        q.append(dup_path)

        return None

    def depth_first_search(self, starting_vertex, target):
        # create a _queue_ FIFO
        stack = []
        visited = []
        # Enqueue the starting vertex
        stack.append(starting_vertex)
        print("stack: ",stack)
        # while the queue is not empty
        while len(stack) > 0:
            # dequeue a node from the queue
            path = stack.pop(0)
            node = path[-1]
            if node not in visited:
                # Mark it as visited
                visited.append(node)
                print("visited depth: ",visited)
                if target in visited:
                    print("Path: ",path)
                    print("Dup_Path: ", dup_path)
                    return dup_path
                # Enqueue all of its children
                for i in self.vertices[node]:
                    if i not in visited:
                        dup_path = list(path)
                        dup_path.append(i)
                        stack.append(dup_path)

        return None


def print_vertex():
    graph = Graph()
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_vertex('5')
    graph.add_vertex('6')
    graph.add_edge_bi('0', '3')
    graph.add_edge_mono('0', '1')
    graph.add_edge_mono('0', '4')
    graph.add_edge_mono('2', '1')
    graph.add_edge_mono('3', '5')
    graph.add_edge_mono('3', '2')
    graph.add_edge_mono('5', '4')
    graph.add_edge_mono('6', '5')
    graph.add_edge_mono('6', '2')
    print("The Vertices: ",graph.vertices)
    for v in graph.vertices['0']:
        print(v)
    print(graph.breadth_first_traverse('0'))
    print(graph.dfr_r('0'))
    print(graph.dft_recurse('0'))
    print(graph.depth_first_search('0', '2'))
    print(graph.breadth_first_search('0', '2'))

print_vertex()
