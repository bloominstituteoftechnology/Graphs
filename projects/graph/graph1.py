# class GraphNode:
#     def __init__(self ,value):
#         self.value = value
#         self.neighbors = []
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
        return len(self.queue)

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
        

 
def dft(start_node) :
    stack = Stack()
    
    visited = set()
    stack.push(start_node)
    while stack.size()>0:
        
        current_node = stack.pop()
        
        if current_node not in visited:
            visited.add(current_node)
            
            neighbors = current_node.neighbors
            
            for n in neighbors:
                stack.push(n)
                
                
def bft(start_node):
    q = Queue()  
    visited = set()  
    #"PRIME THE PUMP" 
    q.enqueue(start_node)
    while q.size()>0:
        
        current_node = q.dequeue()
        
        if current_node not in visited:
            
            visited.add(current_node)
            
            neighbors = start_node.neighbors
            
            for n in neighbors:
                q.enqueue(n)
        
            
     
          