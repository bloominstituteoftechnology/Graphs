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

    def breathFirstSearch(self, start_node):
        # make Q
        queue = Queue()
        # make visit list
        visited_list = set()
        # start node in Q
        queue.enqueue(start_node)
        # while Q !empty
        while queue:
            # remove node from Q
            node = queue.dequeue()
            # visited?
            if node not in visited_list:
                # No? then mark visited
                print(node)
                visited_list.add(node)
                # put children in Q
                for child in self.vertices[node].edges:
                    queue.enqueue(child)

    def depthFirstTraversal(self, starting_node):
        # make  Stack
        stack = Stack()
        # make  visited list
        visited_list = set()
        # start node to stack
        stack.push(starting_node)
        # While Stack !empty
        while stack.size() > 0:
            # Stack - first node
            node = stack.pop()
            # if visited = no
            if node not in visited_list:
                # Mark visited
                print(node)
                visited_list.add(node)
                # put children in stack
                for child in self.vertices[node].edges:
                    stack.push(child)


    def depthFirstTraversal_recursive(self,node, visited_list = None):
        if visited_list is None:
            visited_list = set()
        # set start node visited
        print(node)
        visited_list.add(node)
        # run depthFirstTraversal_recursive on each child
        for child in self.vertices[node].edges:
            if child not in visited_list:
                self.depthFirstTraversal_recursive(child, visited_list)

    def bfs(self, starting_node, destination_node):
        # last element in Q
        # make Queue
        queue = Queue()
        # make visited
        visited_list = set()
        # start node to Q
        queue.enqueue(starting_node)
        # While Queue !empty
        while queue.size() > 0:
            # remove first node
            path = queue.dequeue()
            # If visited = no
            if path[-1] not in visited_list:
                # Mark visited = yes
                if destination_node == path[-1]:
                    return True
                visited_list.add(path[-1])
                # put children in Q
                for child in self.vertices[path[-1]].edges:
                    new_path = list(path)
                    new_path.append(child)
                    queue.enqueue(child)
        return False

    def dfs(self, starting_node, destination_node):
        # last element in stack
        # make empty stack
        stack = stack()
        # make visited list
        visited_list = set()
        # start node to stack
        stack.push(starting_node)
        # While Stack !empty
        while stack.size() > 0:
            # remove first node
            path = stack.pop()
            # If visited = no
            if path[-1] not in visited_list:
                # Mark visited = yes
                if destination_node == path[-1]:
                    return path
                visited_list.add(path[-1])
                # put children in the stack
                for child in self.vertices[path[-1]].edges:
                    new_path = list(path)
                    new_path.append(child)
                    stack.push(child)
        return False

    #depthFirstSearch_recursive
    def depthFirstSearch_recursive(self, starting_node,visited=None, path=None):
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
            # for unvisited child
            if child not in visited:
                # depthFirstSearch_recursive on child
                new_path = self.depthFirstSearch_recursive(child,destination_node,visited, extended_path)
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
graph.depthFirstTraversal_recursive("1")
