"""
Simple graph implementation
"""

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
        return len(self.stack)

# covert this to a link list later
class Queue():
    def __init__(self):
        self.queue = []
    def nq(self, value):
        self.queue.append(value)
    def dq(self):
        if self.size() > 0:
            return self.queue.pop()
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        pass  # TODO

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, edge_one, edge_two):
        if edge_one in self.vertices and edge_two in self.vertices:
            self.vertices[edge_one].add(edge_two)
        else:
            raise IndexError("That vertex does not exist")
        pass
    
    def bft(self, start):
        # create que
        q = Queue()
        # create visited
        visited = set()
        # que the start
        q.nq(start)
        # # while que not empty
        while q.size() > 0:
            # remove item from que
            node = q.dq()
            if node not in visited:
                # mark as visited / add to visited
                visited.add(node) 
                # add children to que
                for next_node in self.vertices[node]:
                    q.nq(next_node)
        print(visited)
        pass
    


tester = Graph()
tester.add_vertex('0')
tester.add_vertex('1')
tester.add_vertex('2')
tester.add_vertex('3')
tester.add_edge('0', '1')
tester.add_edge('0', '3')
tester.bft('0')
