"""
Simple graph implementation
"""
from queue import Queue

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):    # O(1)
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
        
#class Queue:
#    def __init__(self):
#        self.queue = []
#    def enqueue(self, value):
#        self.queue.append(value)
#    def dequeue(self):        # O(n)
#        if self.size() > 0:
#            return self.queue.pop(0)
#        else:
#            return None
#    def size(self):
#        return len(self.queue)
    
    ## Here, the dequeue method is O(n), because if we're removing something from the beginning, we need to move the rest of the list over, so its costly.
    ## The best way is to implement queue using linked list
    ## But for this case, our list isn't too big so its fine.

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}    # empty dictionary
        
    def add_vertex(self, vertex):
        """ Check if the vertex is in vertices; if not, add it. """
        
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
            
    def add_edge(self, vertex_1, vertex_2):
        """ 
        Want directed edges. 
        Check if the vertices are in self.vertices; if yes, add the connection.
        """
        
        if vertex_1 in self.vertices and vertex_2 in self.vertices:
            self.vertices[vertex_1].add(vertex_2)    # vertex_1 -> vertex_2
        else:
            raise IndexError("The vertex does not exist!")
            
    def add_undirected_edge(self, vertex_1, vertex_2):
        if vertex_1 in self.vertices and vertex_2 in self.vertices:
            self.vertices[vertex_1].add(vertex_2)    # vertex_1 -> vertex_2
            self.vertices[vertex_2].add(vertex_1)
        else:
            raise IndexError("The vertex does not exist!")
            
    def breadth_first_traversal(self, starting_node):  # O(n)
        """ 
        Create a queue, the queue is implemented in a separate class.
        Add the start_node to the queue.
        Mark the first node as visited.
        Enqueue the starting node
        While the queue is not empty,
            Dequeue a node from the queue
            Mark it as visited
            Enqueue all of its children
        """
        
        queue = Queue()    # O(1)
        visited = set()
        queue.enqueue(starting_node)	# O(1)
    
        while queue.len() > 0: # O(n)
 
            current_vertex = queue.dequeue()	# O(1)
            
            if current_vertex is None:
                return
            
            if current_vertex not in visited:
                visited.add(current_vertex)	# O(1)
                print(current_vertex)
                for child in self.vertices[current_vertex]:
                    if child is not None:
                        queue.enqueue(child)

    def depth_first_traversal(self, starting_node):
        """ 
        Create a stack (last in, first out) and a set for visited nodes
        Push the starting node
        While the stack is not empty,
            Pop a node from the stack
            Mark it as visited
            Push all of its children that have not been visited
        """
                
        stack = Stack()
        visited = set()
                
        stack.push(starting_node)
        
        while stack.size() > 0:
            current_vertex = stack.pop()
            
            if current_vertex is None:
                return
            
            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)
                for child in self.vertices[current_vertex]:
                    if child is not None:
                        stack.push(child)

    def depth_first_recursion(self, starting_node, queue = Queue(), visited = None):
        """
        Want to pass the visited set around in the recursion, visited = None
        Create visited set if there isn't one already
        Mark the node as visited
        If the node has children and they are not in the visited set, add them and call this method recursively on the unvisited children
        """
        
        queue = queue
        
        if visited is None:
            visited = set()
        
        queue.enqueue(starting_node)
        print(starting_node)
        
        current_vertex = queue.dequeue()
        
        if current_vertex not in visited:
            visited.add(current_vertex)
            
            for child_node in self.vertices[current_vertex]:
                if child_node not in visited:
                    self.depth_first_recursion(child_node, queue, visited)

    def breath_first_search_path(self, starting_node, target_node):
        """
        Want to check to the path (shortest) contains the target node
        Want to record the path that it took to get to a node, by getting the parent node 
        Make a copy of the path and add the children to it
        Enqueue the new path
        """
        
        queue = Queue()
        visited = []
        
        queue.enqueue([starting_node])
        
        while queue.len() > 0:    # .len() is a method in Queue class
            path = queue.dequeue()
            node = path[-1] # last node in path
            
            if node not in visited:
                print(node)
                visited.append(node)
                
                if node == target_node:
                    return path
                
                for next_node in self.vertices[node]:
                    new_path = path.copy()
                    new_path.append(next_node)
                    
                    queue.enqueue(new_path)
                    
        return False
        
    def depth_first_search_path(self, starting_node, target_node):
        """
        For performance, depth first is going to be fast because it's going to give back the first result.
        But breadth first is overall better, even though, it is slower, it's always going to give back the best result.
        Example: Direction to Noshi, but you only get to use the map once to get direction.
            It's better to take a little more time to get the shortest route then the first route available (we don't want a route that will take us from here to New York then back to Noshi).
        """
        
        stack = Stack()
        visited = []
        
        stack.push([starting_node])
        
        while stack.size() > 0:    # .len() is a method in Queue class
            path = stack.pop()
            node = path[-1] # last node in path
            
            if node not in visited:
                print(node)
                visited.append(node)
                
                if node == target_node:
                    return path
                
                for next_node in self.vertices[node]:
                    new_path = path.copy()
                    new_path.append(next_node)
                    
                    stack.push(new_path)
                    
        return False