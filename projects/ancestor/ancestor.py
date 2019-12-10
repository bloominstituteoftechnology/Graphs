
# Importing graph
import sys
sys.path.append('../graph')
from graph import Graph
from util import Queue, Stack


def earliest_ancestor(ancestors, starting_node):
    # Building graph from data coming in
    graph = Graph()
    for d in range(1,12):
        graph.add_vertex(d)
    for pair in ancestors:
        graph.add_edge(pair[0],pair[1])
   
    q = Queue()
    q.enqueue(starting_node)

    check_number = ''   #variable to check against

    print(graph.vertices)
    print(f'STARTING NODE  {starting_node}')
    check_array = [] #check array to check against
    children = [] #children array to check against
    for d in graph.vertices: #for every instance in the graph
        # if graph.vertices[d] != set():  # if that value != set()   aka if it has nodes pointing to it, if it has parents
            while len(graph.vertices[d]) > 0: #while the length of each set is >0
                check_number = graph.vertices[d].pop() #pop of each set item (each child it points to)
  
                check_array.append((check_number, d)) #add that number to the checkarray and append it's parent as the second argument
                children.append(check_number) #just append that popped off item into the children array -- used to check if an item is NOT in it, ergo it is a top node
         
      
    print(check_array)
    for x in check_array: # for every instance in check array
        if x[0] == starting_node: #if the first item (the child) exists, then you will want to grab the parent and call recursion to climb up the tree

            print(f'true, it is here at {x[1]} and does equal {starting_node}')
            if x[1] in children: #if the parent node is a child (not a top node)
                print(f'passing in {x[1]}')
                return earliest_ancestor(ancestors,x[1]) #call recursion on that node
            else:
                return x[1] #if it is not a child, you have reached the top
    return -1 #if none above, it does not exists
                
                
                    
