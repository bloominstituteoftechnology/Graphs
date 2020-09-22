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
def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
a =[(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]   
def earliest_ancestor(ancestors, starting_node):
    checked =[ ]
    stack = Stack()
    stack.push(starting_node)
    
    
    while stack.size()>0:
        
        current = stack.pop()
        
        if current not in checked:
            print(current)
            checked.append(current)
            
            neighbors = self.get_neighbors()
            print(checked[0])
            print(checked)
         
print(earliest_ancestor(a,6))     
         