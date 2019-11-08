from util import Stack
'''
Write a function that takes a 2D binary array and returns the number of 1 islands.
An island consists of 1s that are connected to the north, south, east or west. For example:
'''
# Unweighted
# Undirected 
# Cyclic

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

big_islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
               [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
               [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
               [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
               [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
               [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
               [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]


def get_island_neighbors(x, y, matrix):
    neighbors = []
    # Check if theres a 1 to the north
    if y > 0 and matrix[y - 1][x] ==1:
        neighbors.append( (x, y-1) )
    # Check south
    if y < len(matrix) - 1 and matrix[y + 1][x] == 1:
        neighbors.append( (x, y+1) )
    # Check east
    if x < len(matrix[0]) - 1 and matrix[y][x + 1] == 1:
        neighbors.append( (x + 1, y) )
    # Check west
    if x > 0 and matrix[y][x - 1] == 1:
        neighbors.append( (x - 1, y) )
    return neighbors

def dft_islands(start_x, start_y, matrix, visited):
    '''
    Return and updated visited matrix after a dft of matrix starting from x y
    '''
    # Create an empty stack and enqueue the starting vertex ID
    s = Stack()
    s.push( (start_x, start_y) )
    # While the stck is not empty...
    while s.size() > 0:
        # Pop the first vertex
        v = s.pop()
        x = v[0]
        y = v[1]
        # If that vertex had not been visited...
        if not visited[y][x]:
            # Mark it as 
            visited[y][x] = True
            # Then add all of it's neighbors to the top of the stack
            for neighbor in get_island_neighbors(x, y, matrix): #STUB
                s.push(neighbor)
    return visited


def island_counter(matrix):
    # Create a visited matric with the same dimensions as the islands matrix
    visited = []
    matrix_width = len(matrix)
    matrix_height = len(matrix[0])
    for i in range(matrix_height):
        visited.append( [False] * matrix_width)
    # Create a counter initialize it to 
    counter = 0
    # For each cell in the 2d array
    for x in  range(matrix_width):
        for y in range(matrix_height):
            # If it has not been visited
            if not visited[y][x]:
                # When you come across a 1, 
                if matrix[y][x] == 1:
                    # DFT it and mark all the connected nodes as visited
                    visited = dft_islands(x, y, matrix, visited) #STUB
                    # Then increment a counter
                    counter += 1
    return counter

print('Small islands')
print(island_counter(islands))
print('Big islands')
print(island_counter(big_islands))