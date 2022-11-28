  
    
     
    
islands = [[0,1,0,1,0],
               [1,1,0,1,1],
               [0,0,1,0,0],
               [1,0,1,0,0],
               [1,1,0,0,0]
               ]
def getNeighbors(matrix, node):
    row, col = node
    neighbors = []
    
    if matrix [row][col + 1]>0:
        neighbors.append((row, col +1))
    
    if matrix[row +1][col]>0:
        neighbors.append((row +1, col))

    if matrix[row -1][col]> 0:
        neighbors.append((row -1, col))
        
    return neighbors    
        

def dft_recursive(node, matrix, visited):
    if node not in visited:
       visited.add(node)
       neighbors = getNeighbors(matrix, node)
       for n in neighbors:
           dft_recursive(n, matrix, visited)
        
def island_counter(matrix):
    visited = set()
    total_islands = 0
    for row in range (len(matrix)):
        for col in range(len(matrix[row])) :
            
             
            item = matrix[row][col]
            if item == 1 and (row, col) not in visited:
                total_islands +=1
                visited.add((row, col))
                dft_recursive((row,col), matrix, visited)
                
    return total_islands            
# Iterate over every item
# If its a 1 and hanst been visited:
#     run a traversal
    
print( island_counter(islands)   )