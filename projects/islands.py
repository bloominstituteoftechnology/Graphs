# Write a function that takes a 2D binary array and returns the number of 1 islands.
# An island consists of 1s that are connected to the north, south, east or west OR a 1 by itself. For example:
# islands = [[0, 1, 0, 1, 0],
        #    [1, 1, 0, 1, 1],
        #    [0, 0, 1, 0, 0],
        #    [1, 0, 1, 0, 0],
        #    [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4

#Steps:
# Step 1: Describe in graphs terminology
#-- What are our nodes? the ones
#-- What are our connections(when do we have an edge to another node)? If one step away, to NSEW
#-- What do we call a group of 1s/nodes? Connected components

# 2) Build your graph OR define a get_neighbors function

# 3) Choose your graph algorithm and run 


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

# Brian's suggestions

# list out keywords that seem important:
# islands consists of - connected components
# connected - neighbors (edges)
# directions - N S E W (edges)
# 2d Array - more or less the graph
# returns(shape of solution) - the number of islands

# how can we write a get neighbor function that uses the shape? - offset the coordinates

# how can we find the extent of the island? - can use BFT or DFT to find all of the nodes in an island - use traversal because we want to touch every node

# how do I expolre a larger set? - loop through and call a traversal if we find an unvisited 1 (nested loop)


def getNeighbors(node, islands):
    row, col = node #example of tuple unpacking
    
    stepNorth = stepSouth = stepEast = stepWest = None
    
    neighbors = []
    
    if row > 0:
        stepNorth = row - 1
    
    if row < len(islands) - 1:
        stepSouth = row + 1
    
    if col < len(islands) - 1:
        stepEast = col + 1

    if col > 0:
        stepWest = col - 1
        
    if stepNorth is not None and islands[stepNorth][col] == 1:
        neighbors.append((stepNorth, col))
    
    if stepSouth is not None and islands[stepSouth][col] == 1:
        neighbors.append((stepSouth, col))
        
    if stepWest is not None and islands[row][stepWest] == 1:
        neighbors.append((row, stepWest))

    if stepEast is not None and islands[row][stepEast] == 1:
        neighbors.append((row, stepEast))
        
    return neighbors
        
        
def dft_recursive(node, visited, islands):
    if node not in visited:
        visited.add(node)
        
        neighbors = getNeighbors(node, islands)
        
        for neighbor in neighbors:
            dft_recursive(neighbor, visited, islands)


def island_counter(islands):
    total_islands = 0
    visited = set()
    #iterate over the matrix
    for row in range(len(islands)):
        for col in range(len(islands)):
            # when we hit a 1
            if islands[row][col] == 1 and node not in visited:
                # increment counters
                total_islands += 1            
                # run DFT on it and mark as visited
                dft_recursive(node)
    
    return total_islands       
            

print(island_counter(islands))