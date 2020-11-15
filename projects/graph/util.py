
# Note: This Queue class is sub-optimal. Why?
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

def map_array(array):
    for node in array:
        

def return_neighbors(node):
    

def earliest_ancestor(ancestors, starting_node):
    # depth first search / traversal
    stack = Stack()
    stack.push({
        'current_node': starting_node,
        'path': [starting_node]
    })

    visited = set()

    while stack.size() > 0:
        current_object = stack.pop()
        current_path = current_object['path']
        current_node = current_object['current_node']
        
        if current_node not in vistited:
            
            visited.add(current_node)
            
            for neighbor in 
            
            
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]            
            
