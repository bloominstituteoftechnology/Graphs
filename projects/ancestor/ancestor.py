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
#  \ /   / \ / <--The edge is the relationship that connects the two vertices(nodes)
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
#When we input a child, we want to traverse what is before it not after
#If a descendent was the input, then we would traverse downward, the input, in this case, are ancestors, which means we traverse upwards or backwards
#How?
#The starting node(child) has to be the last vertex from the bottom. Therefore set the first vertex to be the 
#We'll call each vertex the parent 
#The condition here is find to find the earliest ancestor, therefore the first question is does the parent have more parents.  If yes, queue the parents.  If no parents == earliest ancestor




#Need to find the ancestor that is furthest away from the starting node. So everytime a node is visited, the distance +=1
#Therefore if the path is 
