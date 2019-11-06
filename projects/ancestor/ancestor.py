import sys
sys.path.append('../graph')
from graph import Graph
from util import Queue, Stack


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for d in range(1,12):
        graph.add_vertex(d)
    for pair in ancestors:
        graph.add_edge(pair[0],pair[1])
   
    # # Create an empty queue and enqueue the starting vertex ID
    # print(starting_node)
    
    q = Queue()
    q.enqueue(starting_node)
    # Create a Set to store visited vertices
   
    visited = set()
    # While the queue is not empty...
    # print(graph.vertices)
    # print(graph.vertices)
    sample = graph.vertices[5]
    # print(sample)
    check_number = ''
    # print(graph.vertices)
    # removed = ''
    # print(graph.vertices)
    print(f'STARTING NODE  {starting_node}')
    check_array = []
    # print(graph.vertices[2])
    parents = []
    children = []
    for d in graph.vertices:
        if graph.vertices[d] != set():
            
            # print(f'{d}: {graph.vertices[d]}')
            
            while len(graph.vertices[d]) > 0:
                check_number = graph.vertices[d].pop()
                # print(f'popped of {check_number}')
                check_array.append((check_number, d))
                children.append(check_number)
                parents.append(d)
            #    checked[check_number] = d
            # print(check_array)
            # print(parents)
            # print(check_array)
    print(check_array)
    for x in check_array:
        if x[0] == starting_node:
            print(f'true, it is here at {x[1]} and does equal {starting_node}')
            if x[1] in children:
                # new_pass = x[1]
                print(f'passing in {x[1]}')
                return earliest_ancestor(ancestors,x[1])
            else:
                return x[1]
    return -1
                
                
                    
                    # print(x)
            # if starting_node in check_array:
            #     for x in check_array:
                    # if x == starting_node:
                    #     print(x)
            #     print(d)
            #     if check_number == starting_node:
            #         break
                
            # # print(f'current is {starting_node}')
            # if check_number == starting_node:
            #     # print(f'passing in {d}')
            #     earliest_ancestor(ancestors, d)
            
    # return -1
            

        
    # while q.size() > 0:
    #     # Dequeue the first vertex
    #     v = q.dequeue()
    #     # print(graph.vertices[1])
    #     # If that vertex has not been visited...
    #     if v not in visited:
    #         # Mark it as visited...
    #         visited.add(v)
    #         # print(v)
    #         # print(graph.vertices[1])
    #         for neighbor in graph.vertices[v]:
    #             # print(neighbor)
    #             q.enqueue(neighbor)

               
            # Then add all of its neighbors to the back of the queue
