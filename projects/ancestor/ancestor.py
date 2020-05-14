#1. Import the Queues and Stacks to draw from that file.
#2. Import graph.py from Graph folder
from util import Stack, Queue
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    q = Queue()
    q.enqueue([starting_node])

    #Keep track of the visiting nodes
    visited = set()

    #Keep going until the queue is empty
    while q.size() > 0:
        #Dequeue first vert
        #print(q.queue)
        path = q.dequeue()
        v = path[-1]
         #If it's not visited
        if v not in visited:

            #Mark visited
            visited.add(v)
            if v == ancestors:
                return path
                for next_vert in g.get_neighbors(v):
                    new_path = path.copy()
                    new_path.append(next_vert)
                    q.enqueue(new_path)


#     10
#  /
# 1   2   4  11
#  \ /   / \ /
#   3   5   8
#    \ / \   \
#     6   7   9
# ```

# Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.

#Setup

#1. Import the Queues and Stacks to draw from that file.
#2. Import graph.py from Graph folder
#3. Check testing 
#4. How to implement a BFS to locate earliest ancestor 

#Implementation
#Given a data set (like visited = set())
