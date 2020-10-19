from util import Queue

def get_ancestor(ancestors, child):
    heirs = []
    for heir in ancestors:
        if heir[1] == child:
            heirs.append(heir[0])
    return heirs

def earliest_ancestor(ancestors, starting_node):
    #create empty queue
    q = Queue()
    #add starting node to queue
    q.enqueue([starting_node])
    #create set to store visited vertices
    visited = set()
    #initialize path length
    path_len = 1
    #sets oldest parent as -1 for if no parent
    oldest_parent = -1

    #while size of q is greater than 0
    while q.size() > 0:
        #dequeue first path
        path = q.dequeue()
        #grab the last vertex from the path
        cur_node = path[-1]

        #if that vertex has not been visited
        if cur_node not in visited:
            #mark as visited
            visited.add(cur_node)
        
        #check for need to update
        if len(path) >= path_len and cur_node <oldest_parent or len(path) > path_len:
            #updates path length
            path_len = len(path)
            #updates oldest parent
            oldest_parent = cur_node

        #then add a path to its parent to the back of the queue
        for parent in get_ancestor(ancestors, cur_node):
            #copy path
            path_copy = list(path)
            #append parent to the back
            path_copy.append(parent)
            q.enqueue(path_copy)

    return oldest_parent