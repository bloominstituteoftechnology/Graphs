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


def create_adjacency_list(alsit):
    al = {}
    for k,v in alsit:
        if v not in al:
            al[v] = k
    return al



def earliest_ancestor(ancestors, starting_node):
    #get adjacency list of ancestors
    ancestors = create_adjacency_list(ancestors)
    # print(ancestors[10])
    #create stack for longest ancestral line
    s = Stack()
    # create visited set
    visited = set()
    #add start to stack
    s.push(starting_node)

    if starting_node not in ancestors:
        return -1

    while s.size() > 0:
        #get current ancestor from stack
        current_ancestor = s.pop()
        # print(current_ancestor)
        #check if current in visited
        if current_ancestor not in visited:
            visited.add(current_ancestor)
 

            if current_ancestor not in ancestors:
                return current_ancestor
            #push new neighbors
            else:
                s.push(ancestors[current_ancestor])

     



    
    

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors,6)
