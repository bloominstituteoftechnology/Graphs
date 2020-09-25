#What are our nodes? nums/people

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
    def size (self):
        return len(self.queue)    

class Graph:
    def __init__(self):
        self.verts = {} # adj list (dictionary) of vertices mapping labels to edges

    def add_vertex(self, vertex_id):
        if vertex_id not in self.verts:
            self.verts[vertex_id] = set()
    
    def add_edge(self, v1, v2):
        if v1 in self.verts and v2 in self.verts:
            self.verts[v1].add(v2)
            
def getParents(ancestors, node):
    parents = []
    for pair in ancestors:
        if pair[1]==node:
            parents.append(pair[0])
    return parents        

def dft_recursive(ancestors, node, distance):
    print(node, distance)
    parents = getParents(ancestors ,node)
    
    aged_one = (node, distance)
    
    for parent in parents:
        pair = dft_recursive(ancestors, parent, distance +1)
        print(pair, aged_one)
        if pair[1]> aged_one[1]:
            aged_one = pair
    return aged_one
    
def earliest_ancestor(ancestors, starting_node, distance = 0):
    aged_one = dft_recursive(ancestors, starting_node, distance)
    
    if aged_one[0] == starting_node:
        return -1
    
    return aged_one
        
     
     ## modify it so as you go, you keep track of the node that's farthest away.
        
a =[(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]   
         
print(earliest_ancestor(a,1))     
         