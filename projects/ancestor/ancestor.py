from queue import Queue

def build_graph(anscestors):
    # will loop throught the anscestors and will 
    # build the graph
    graph = {}
    for parent, child in anscestors:
        if child not in graph:
            graph[child] = set()
        graph[child].add(parent)
    return graph

def earliest_ancestor(ancestors, starting_node):
    
    
    graph = build_graph(ancestors)

    if starting_node not in graph:
        return -1

    # will now go through by bft
    path = [starting_node]
    my_queue = Queue()
    generation = {} # this is a dictionary that will hold the 
                    # generation of the earliest anscestor as the key and 
                    # the val is the earlies anscestor 
    gen_count = 0
     # putting the path with the starting node in the queue
    my_queue.put(path)

    # will now do the while loop
    # in here will dequeue and then look for the neighbors
    # if they have not been visited then we will put them then we 
    # won't add them.
    while my_queue.qsize() > 0:
        # dequueing
        curPath = my_queue.get()
        gen_count = len(curPath)-1 # this to keep track of the generation count that we are on for each 
                                   # of the paths
        # need to check if there are any neighbors
        if curPath[-1] not in graph: # this means that there are no neighbors
            # will put the end of the path in dictionary
            if gen_count not in generation:
                generation[gen_count] = set()
            generation[gen_count].add(curPath[-1])
            continue # continuing to the front of the while loop 
        # if there are neighbors will be down here
        for n in graph[curPath[-1]]:
            newPath = curPath[:]
            newPath.append(n)
            # putting it in the queue
            my_queue.put(newPath)
    # now we need to find out what the last gen count was
    returnVal = 11111111111111111110
    for val in generation[gen_count]: # giving it the last generation count
                                      # so that we are looking at the earliest generation
        if returnVal > val:
            returnVal = val
    return val
        
     
    
    

    