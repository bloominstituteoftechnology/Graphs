"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        # initialize verticies to an empty dictionary
        self.verticies = {}
    # add_vertex method to create node or vertex and initialize the vertex id to an empty set()

    def add_vertex(self, vertex_id):
        # key of the specific vertex will be vertex_id, while the edges will be initialized to the empty set
        self.verticies[vertex_id] = set()
    # add_directed_edge method to create edges or connections from vertex1 to vertex2, one way

    def add_directed_edge(self, v1, v2):
        # check to see if v1 and v2 are both valid values or actual verticies in the graph
        if v1 in self.verticies and v2 in self.verticies:
            # if valid verticies, from v1 add v2 to the set, only one way or directed
            self.verticies[v1].add(v2)
        # if the provided v1 or v2 does not exist raise error
        else:
            raise IndexError("That vertex does not exist")
    # add_undirected_edge method to create edges or connections from vertex1 to vertex2, both ways

    def add_undirected_edge(self, v1, v2):
        # check to see if v1 and v2 are both valid values or actual verticies in the graph
        if v1 in self.verticies and v2 in self.verticies:
            # if valid verticies, from v1 add v2 to the set
            self.verticies[v1].add(v2)
            # then add from v2 to v1 to the set, this allows the connection both ways
            self.verticies[v2].add(v1)
        # if the provided v1 or v2 does not exist raise error
        else:
            raise IndexError("That vertex does not exist")

    # add a breadth first traversal method which takes a starting vertex as an argument
    # to do this first create a queue class which would be a first in first out data structure
    def bft(self, starting_vertex_id):
        # initialize an empty queue for breadth first traversal
        queue = Queue()
        # initialize an empty set of visited verticies
        visited = set()
        # put the starting vertex into the queue
        queue.enqueue(starting_vertex_id)
        # while the queue is not empty traverse the graph
        while queue.size() > 0:
            # dequeue the value at the start of the queue and assign it to vertex
            vertex = queue.dequeue()
            # if the vertex has not already been visited add it to the visited set
            if vertex not in visited:
                print(vertex)
                # mark as visited
                visited.add(vertex)
                # put the verticies that are connected to the current vertex into the queue
                for neighbor in self.verticies[vertex]:
                    # enqueue the values of the verticies set for the current vertex into the queue
                    queue.enqueue(neighbor)

    # add a depth first traversal method which takes a starting vertex as an argument
    # to do this first create a stack class which would be a last in first out data structure

    def dft(self, starting_vertex_id):
        # initialize an empty stack for depth first traversal
        stack = Stack()
        # initialize an empty set of visited verticies
        visited = set()
        # push the starting vertex into the stack
        stack.push(starting_vertex_id)
        # while the stack is not empty traverse the graph
        while stack.size() > 0:
            # pop the value at the end of the stack and assign it to vertex
            vertex = stack.pop()
            # if the vertex has not already been visited add it to the visited set
            if vertex not in visited:
                print(vertex)
                # mark as visited
                visited.add(vertex)
                # put the verticies that are connected to the current vertex into the stack
                for neighbor in self.verticies[vertex]:
                    # push the values of the vertecies set for the current vertex into the stack
                    stack.push(neighbor)

    # add a depth first traversal method using recursion which takes a starting vertex as an argument, and an empty visited list
    def dftr(self, starting_vertex_id, visited=[]):
        # initialize the visited list with the starting vertex, we will keep adding to this list with the recursive calls
        visited += [starting_vertex_id]
        # check the values or neighbors for the starting vertex
        for neighbor in self.verticies[starting_vertex_id]:
            # if the neighbor is not in the visited list, recursively call the depth first search recursive method and pass in the neighbors and the visited list
            if neighbor not in visited:
                # assign visited to the value of the recursive call while passing in the neighbor values and the visited list
                visited = self.dftr(neighbor, visited)
        # return the visited list
        return visited

    # breadth first search method takes a starting vertex and destination vertex as arguments and returns shortest path from starting vertex to destination vertex
    def bfs(self, starting_vertex_id, destination_vertex_id):
        # initialize an empty queue for breadth first search
        queue = Queue()
        # initialize an empty set of visitied verticies
        visited = set()
        # put the starting vertex into the queue
        queue.enqueue(starting_vertex_id)
        # while the queue is not empty traverse the graph
        while queue.size() > 0:
            # dequeue the value at the start of the queue and assign it to path
            path = queue.dequeue()
            print(f'path: {path}')
            # assign the vertex or current node to the last vertex of path
            vertex = path[-1]
            # if the vertex has not already been visited add it to the visited set
            if vertex not in visited:
                print(f'vertex: {vertex}')
                # mark as visited
                visited.add(vertex)
                # put the verticies that are connected to the current vertex into the queue
                for neighbor in self.verticies[vertex]:
                    # assign route to a list and pass in path
                    route = list(path)
                    print(f'route: {route}')
                    # append the neighbor to route
                    route.append(neighbor)
                    print(f'route after append: {route}')
                    # enque the value of the route to the queue
                    queue.enqueue(route)
                    # once the destination vertex is reached return the route
                    if neighbor == destination_vertex_id:
                        return route
                    # if destination cannot be reached, return error
                    else:
                        return "cannot reach destination"

    # depth first search method takes a starting vertex and destination vertex as arguments and returns a valid path from starting vertex to destination vertex

    def dfs(self, starting_vertex_id, destination_vertex_id):
        # initialize an empty stack for depth first search
        stack = Stack()
        # initialize an empty set of visited verticies
        visited = set()
        # push the starting vertex into the stack
        stack.push(starting_vertex_id)
        # while the stack is not empty traverse the graph
        while stack.size() > 0:
            # pop the value at the end of the stack and assign it to path
            path = stack.pop()
            print(f'path: {path}')
            # assign the vertex or current node to the last vertex of path
            vertex = path[-1]
            # if the vertex has not already been visited add it to the visited set
            if vertex not in visited:
                print(f'vertex: {vertex}')
                # mark as visited
                visited.add(vertex)
                # put the verticies that are connected to the current vertex into the stack
                for neighbor in self.verticies[vertex]:
                    # assign route to a list and pass in path
                    route = list(path)
                    print(f'route: {route}')
                    # append the neighbor to route
                    route.append(neighbor)
                    print(f'route after append: {route}')
                    # push the value of the route to the stack
                    stack.push(route)
                    # once the destination vertex is reached return the route
                    if neighbor == destination_vertex_id:
                        return route
                    # if destination cannot be reached return error
                    else:
                        return "cannot reach destination"


# queue class, first in first out data structure
class Queue():
    def __init__(self):
        # initialize queue as an empty list / array
        self.queue = []
    # create an enqueue method to add a value to the queue

    def enqueue(self, value):
        # append the value to the end of the queue
        self.queue.append(value)
    # create a dequeue method to pop the start value of the queue

    def dequeue(self):
        # check to see if the length of the queue is greater than zero
        if self.size() > 0:
            # if length of queue is greater than zero, pop the value at the start of the queue and return it
            return self.queue.pop(0)
        # if length of queue is 0 return none
        else:
            return None
    # add method to check length of queue

    def size(self):
        return (len(self.queue))


# stack class, last in first out data structure
class Stack():
    def __init__(self):
        # initialize the stack as an empty list / array
        self.stack = []
    # create a push method to add a value to the stack

    def push(self, value):
        # append the value to the end of the stack
        self.stack.append(value)
    # create a pop method to pop the end value of the stack

    def pop(self):
        # check to see if the length of the stack is greater than zero
        if self.size() > 0:
            # if the length of stack is greater than zero, pop the value at the end of the stack and return it
            return self.stack.pop()
        # if the length of the stack is 0 return none
        else:
            return None
    # add method to check length of stack

    def size(self):
        return (len(self.stack))


# test graph
graph = Graph()  # instantiate graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_vertex('8')
graph.add_vertex('9')
graph.add_vertex('10')
graph.add_vertex('11')
graph.add_vertex('12')
graph.add_vertex('13')
graph.add_vertex('14')
graph.add_vertex('15')
graph.add_directed_edge('0', '1')
graph.add_directed_edge('0', '2')
graph.add_directed_edge('0', '3')
graph.add_directed_edge('1', '4')
graph.add_directed_edge('1', '5')
graph.add_directed_edge('4', '6')
graph.add_directed_edge('3', '7')
graph.add_directed_edge('3', '8')
graph.add_directed_edge('7', '9')
graph.add_directed_edge('7', '10')
graph.add_directed_edge('8', '11')
graph.add_directed_edge('8', '12')
graph.add_directed_edge('11', '13')
graph.add_directed_edge('11', '14')
graph.add_directed_edge('13', '15')
# print(graph.verticies)
# test for non existing vertex
# graph.add_directed_edge('0', '4')
# print(graph.verticies)
# print(graph.dft('0'))
# print(graph.bft('0'))
# print(graph.dftr('0'))
# print(graph.bfs('0', '17'))
# print(graph.dfs('0', '17'))
