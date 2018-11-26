import random
import queue
"""
Simple graph implementation compatible with BokehGraph class.
"""

# lecture solution
"""
Simple graph implementation compatible with BokehGraph class.
"""


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if (self.size()) > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if (self.size()) > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:
    # Represent a graph as a dictionary of vertices mapping labels to edges.
    def __init__(self):
        # Create an empty graph
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # Add an vertex to the graph
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, v1, v2):
        """
        Add an undirected edge to the graph
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exist!")

    def add_directed_edge(self, v1, v2):
        """
        Add a directed edge to the graph
        """
        if v1 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def dft(self, starting_node, visited=None):
        # Mark the node as visited
        if visited is None:
            # quese of visited nodes
            visited = []
        visited.append(starting_node)
        # For each child, if that child hasn't been visited, call dft() on that node
        for node in self.vertices[starting_node].edges:
            if node not in visited:
                self.dft(node, visited)

        return visited
        # for child in children:
        #    if child not in visited:
        # dft(child, visted)

    def bft(self, starting_node):
        # create an empty queue
        q = Queue()
        # Put starting vert in the queue
        q.enqueue(starting_node)
        seen = []
        # while q.size() > 0:
        while q.size() > 0:
                    # Remove the first node from the queue...
            new_node = q.dequeue()
            print(new_node)
            # If it has not been visited yet,...
            if new_node not in seen:
                # Mark it as visited....
                seen += new_node
                print(new_node)
            # Then put all it's children in the back of the queue
            q.queue.extend(self.vertices[new_node].edges)
        return seen

    """
    # Stack
    def dft_s(self, starting_node):
        # create an empty stack
        s = Stack()
        # Put starting vert in stack
        s.push(starting_node)
        visited = []
        while s.size() > 0:
            # Pop the first node off the Stack
            # If it has not been visited yet
            #Mark it as visited....
            # Then put all it's children on top of the stack.
    """

    def bfs(self, starting_node, target_node):
        # this is a search not a traversal, hence
        # target node
        visited = []
        # create a queue:
        q = Queue()
        # put starting node into Queue
        q.enqueue(starting_node)
        while q.size() > 0:
            # REMOVE first element from queue
            dequeued = q.dequeue()
            # mark as visited and put into visited list
            visited.append(dequeued)
            # keep track of what we find in our graph
            print(dequeued)
            # if we found the target node, here if we popped into Queue
            if dequeued == target_node:
                return True
                # return True
            '''
            # else iterate through the connceted components
            # sicne we need to look at what is connected by an edge
            # otherwise we won't be properly traversing the graph, and would be
            # looking simply at all the nodes
            # remember so far we have only put the starting node into the queue
            which is declared as a parameter in the function call
            so this last part will run duinng the while look after the
            if statement runs. the loop will run only once:
                iff target_node == starting_node
            '''
            for edge in self.vertices[dequeued].edges:
                # since I'm confused as to how the types don't match
                # aren't edges tuples?
                # while nodes are ints or sinlge bits of an array given that we
                # are using append
                print(' there are the edges', edge)
                print(self.vertices)
                print(self.vertices[dequeued].edges)
                # so it must iterate through self.vertices.edges and get each
                # vertex because self.vertices at [dequeue] is one ver
                # if the child is not in visitied
                if edge not in visited:
                    # put it into the back of the queue so the while runs
                    q.enqueue(edge)
        # if the while fails obviously it's not here
        return False


class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
        """
        Create an empty vertex
        """
        self.id = vertex_id
        self.edges = set()
        if x is None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y is None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y

    def __repr__(self):
        return f"{self.edges}"


# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges.
#     def __init__(self):
#         self.vertices = {}
#     def add_vertex(self, value):
#         if value not in self.vertices:
#             self.vertices[value] = set()
#         else:
#             print("you already have that vertex in this graph")
#     def add_edge(self, v1, v2):
#         self.vertices[v1].add(v2)
#         self.vertices[v1].add(v2)


graph = Graph()
# graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_edge('5', '2')
graph.add_edge('5', '6')
graph.add_edge('2', '1')
graph.add_edge('2', '4')
graph.add_edge('4', '3')
graph.add_edge('6', '7')
#
# print(graph.dft('0'))
# print(graph.bft('0'))
print(graph.bfs('5', '3'))
