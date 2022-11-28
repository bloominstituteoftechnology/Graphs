from graph import Graph

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

def earliest_ancestor(ancestors, starting_node):
    graphed_ancestors = Graph()

    #create vertices for each item in tuple, add edge between them
    for duo in ancestors:
        graphed_ancestors.add_vertex(duo[0])
        graphed_ancestors.add_vertex(duo[1])
        graphed_ancestors.add_edge(duo[1], duo[0])

#bfs
    q = Queue()
    #create a list with starting node to create path
    q.enqueue([starting_node])
    max_paths = 1
    ea = -1

    while q.size() > 0:
        seen = q.dequeue()
        cur = seen[-1]
    
        if len(seen) > max_paths:
            max_paths = len(seen)
            ea = cur
        elif len(seen) >= max_paths and cur < ea:
            ea = cur
            print("*", ea)
            max_paths = len(seen)
        
        for neighbor in graphed_ancestors.get_neighbors(cur):
            q.enqueue(seen + [neighbor]) 
    return ea

    # {[1,2,3,4] [5]} 