"""
Simple graph implementation
"""
class Vertex:
    def __init__(self,vertex_id):
        self.id = vertex_id
        self.edges = set()

class Queue:
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
        return len(self.queue)

class Stack:
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

# make Stack class

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self,vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
                self.vertices[vertex1].edges.add(vertex2)
                self.vertices[vertex2].edges.add(vertex1)

    def add_directed_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].edges.add(vertex2)
    
    def bft(self, start_node):
        # create a queue
        queue = Queue()
        # create a visited list
        visited_list = set()
        # put the start node in the queue
        queue.enqueue(start_node)
        # while queue is not empty...
        while queue:
            # remove node from queue
            node = queue.dequeue()
            # check if it's visited
            if node not in visited_list:
                # if not, mark node as visited
                print(node)
                visited_list.add(node)
                # then put all children in queue
                for child in self.vertices[node].edges:
                    queue.enqueue(child)
        
    def dft(self, starting_node):
        # Create an empty Stack
        stack = Stack()
        # Create an empty visited list
        visited_list = set()
        # Add the start node to the stack
        stack.push(starting_node)
        # While the Stack is not empty...
        while stack.size() > 0:
            # remove the first node from the Stack
            node = stack.pop()
            # If it hasnt been visited
            if node not in visited_list:
                # Mark it as visited
                print(node)
                visited_list.add(node)
                # then put all its children in the stack
                for child in self.vertices[node].edges:
                    stack.push(child)
        
    # recursive dft
    def dft_recursive(self,node, visited_list = None):
        if visited_list is None:
            visited_list = set()
        # Mark starting_node as visited
        print(node)
        visited_list.add(node)
        # Then call dft_recursive on each child
        for child in self.vertices[node].edges:
            if child not in visited_list:
                self.dft_recursive(child, visited_list)

    def bfs(self, starting_node, destination_node):
        # we want last element in q
        # Create an empty Queue
        queue = Queue()
        # Create an empty visited list
        visited_list = set()
        # Add the start node to the queue
        queue.enqueue(starting_node)
        # While the Queue is not empty...
        while queue.size() > 0:
            # remove the first node from the Queue
            path = queue.dequeue()
            # If it hasnt been visited
            if path[-1] not in visited_list:
                # Mark it as visited
                if destination_node == path[-1]:
                    return True
                visited_list.add(path[-1])
                # then put all its children in the queue
                for child in self.vertices[path[-1]].edges:
                    new_path = list(path)
                    new_path.append(child)
                    queue.enqueue(child)
        return False

    def dfs(self, starting_node, destination_node):
        # we want last element in Stack
        # Create an empty Stack
        stack = stack()
        # Create an empty visited list
        visited_list = set()
        # Add the start node to the Stack
        stack.push(starting_node)
        # While the Stack is not empty...
        while stack.size() > 0:
            # remove the first node from the Stack
            path = stack.pop()
            # If it hasnt been visited
            if path[-1] not in visited_list:
                # Mark it as visited
                if destination_node == path[-1]:
                    return path
                visited_list.add(path[-1])
                # then put all its children in the Stack
                for child in self.vertices[path[-1]].edges:
                    new_path = list(path)
                    new_path.append(child)
                    stack.push(child)
        return False

    #dfs_recursive
    def dfs_recursive(self, starting_node,visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        print(starting_node)
        visited.add(starting_node)
        extended_path = list(path)
        extended_path.append(starting_node)
        if starting_node == destination_node:
            return extended_path
        for child in self.vertices[starting_node].edges:
            # for each unvisited child
            if child not in visited:
                # call dfs_recursive on that child
                new_path = self.dfs_recursive(child,destination_node,visited, extended_path)
                if new_path:
                    return new_path
        return None




graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.dfs("1","3")
graph.dft_recursive("1")
