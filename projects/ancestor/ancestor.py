import sys
sys.path.append('../graph')

from util import Stack, Queue

def get_neighbours(ancestors, current_node):
    neighbours =[]
    for tuple_pair in ancestors:  
        if tuple_pair[1] == current_node:
            #if tuple_pair[1] in neighbours:
            neighbours.append(tuple_pair[0])
    if len(neighbours)>1:
        return [min(neighbours)]
    else:
        return neighbours




def earliest_ancestor(ancestors, starting_node):
    #use Bft to find the ancestor
    #if the current node has no neighbour return -1
    if  len(get_neighbours(ancestors, starting_node)) ==0 :
        return -1
    #create a queue
    queue = Queue()
    #add start word to it
    queue.enqueue([starting_node])
    #create a visited set
    visited = []
    #while queue is not empty
    while queue.size()>0:
          #pop the current node off the queue
          current_path = queue.dequeue()
          current_node = current_path[-1]
          #if word has not been visited
          if current_node not in visited:
            #add the current node to visited set
            visited.append(current_node)
            #add neighbours of  the current node to the queue
            for neighbours in  get_neighbours(ancestors, current_node):      
                new_path = list(current_path) 
                new_path.append(neighbours)
                queue.enqueue(new_path)
    return visited[-1]
                

ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(get_neighbours(ancestors, 8))

print(earliest_ancestor(ancestors, 8))
