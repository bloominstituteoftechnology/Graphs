"""
Write a function that takes a 2D binary array and 
returns the number of 1 islands. 
An island consists of 1s that are connected to the 
north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
island_counter(islands) # returns 4


"""
#Translate the problem into terminology you've learned this week
#Build your graph
#Traverse your graph

def island_counter(matrix): 
    #create a visited matrix
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    island_count = 0
    #for all nodes: 
    for col in range(len(matrix[0])): 
        for row in range(len(matrix)):
            