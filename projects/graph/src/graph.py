"""
Simple graph implementation
"""

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return(len(self.queue))

class Stack():
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
        return (len(self.stack))


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex doesn't exist")

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex doesn't exist")

    def breadth(self, starting_vertex_id):
        #create an empty queue
        q = Queue()
        #create and empty set of visited vertices
        visited = set()
        #put the starting vertex in our queue
        q.enqueue(starting_vertex_id)
        #while the queue is not empty
        while q.size() > 0:
            #dequeue the first node from the queue
            v = q.dequeue()
            #if that node has not been visited
            if v not in visited:
                #mark it as visited
                print(v)
                visited.add(v)
                #put all of the children into the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    def depth(self, starting_vertex_id):
        #create an empty stack 
        s = Stack()
        #create an empty set of visited vertices
        visited = set()
        #put the starting vertex in our stack
        s.push(starting_vertex_id)
        #while the stack is not empty
        while s.size() > 0:
            #pop the top node from the stack 
            v.s.pop()
            #if that node has not been visited
            if v not in visited:
                #mark it as visited 
                print(v)
                visited.add(v)
                #then put al of its children into the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)

    def depth_recursion(self, starting_vertex, path=[]):
        path += [starting_vertex]
        print(path)
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in path:
                path = self.depth_recursion(neighbor, path)
        return path

    def breadth(self, start, end):
        verts = self.vertices
        #maintain a queue of paths
        queue = []
        #push the first path into the queue
        queue.append([start])
        while len(queue) > 0:
            #get the first path from the queue
            path = queue.pop(0)
            #get the last node from the path
            node = path[-1]
            #path found
            if node == end:
                return print("Path", path)
            #enumerate all adjacent nodes, construct a new path and push it into the queue
            for adjacent in verts.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
        return 'Destination vertex could not be reached from starting point'

    def depth(self, start, end):
        # Create an empty stack
        s = Stack()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Stack
        s.push(start)
        # While the value passed as "end" is not in the visit array....
        while end not in visited:
            # Pop the top node from the stack
            v = s.pop()
            # If that node has not been visted...
            if v not in visited:
                    # Mark it as visited
                visited.add(v)
                # Then, put all of it's children into the stack
                if v is not None:
                    for neighbor in self.vertices[v]:
                        s.push(neighbor)
                else:
                    return print("they don't connect")
    

graph = Graph()  # Instantiate your graph
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_directed_edge('5', '3')
graph.add_directed_edge('6', '3')
graph.add_directed_edge('7', '1')
graph.add_directed_edge('4', '7')
graph.add_directed_edge('1', '2')
graph.add_directed_edge('7', '6')
graph.add_directed_edge('2', '4')
graph.add_directed_edge('3', '5')
graph.add_directed_edge('2', '3')
graph.add_directed_edge('4', '6')

graph.breadth("2", "6")