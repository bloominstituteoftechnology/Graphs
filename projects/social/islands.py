'''
Write a function that takes a 2D binary array and returns the number of 1 islands. 
An island consists of 1s that are connected to the north, south, east or west. 
For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4

# 1. Is this a graphs problem? If so, translate into graph terminology.
2. Build the graph
3. Traverse the graph

Understand
Plan
E
R
'''
from util import Stack


def island_counter(matrix):
    # Create a visited matrix of the same dimensions as the given matrix
    visited = []
    island_count = 0
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    # Walk through each cell of the matrix
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            # Count up the connected components
            # If it has not been visited...
            if not visited[row][col]:    
                # When I reach a 1...
                if matrix[row][col] == 1:
                    # Do a DFT and mark each 1 as visited
                    visited = dft(col, row, matrix, visited)
                    # Increment the counter by 1
                    island_count += 1
                else:
                    visited[row][col] = True

    return island_count


def dft(col, row, matrix, visited):
    # Create Stack
    s = Stack()
    # Push starting node
    s.push((col,row))
    # While stack is not empty
    while s.size() > 0:
        # Pop vertex from top of the stack
        v = s.pop()
        col = v[0]
        row = v[1]
        # Check if it's visited...
        if not visited[row][col]:
            # Mark it as visited
            visited[row][col] = True
            # Push each neighbor onto the top of the stack
            for neighbor in get_neighbors((col,row), matrix): # STUB
                s.push(neighbor)
    return visited


def get_neighbors(vertex, graph_matrix):
    col = vertex[0]
    row = vertex[1]
    neighbors = []
    # Check north
    if (row > 0 and graph_matrix[row-1][col] == 1):
        neighbors.append((col, row-1))
    # Check south
    if (row < len(graph_matrix) - 1 and graph_matrix[row+1][col] == 1):
        neighbors.append((col, row+1))
    # Check east
    if (col < len(graph_matrix[0]) - 1 and graph_matrix[row][col+1] == 1):
        neighbors.append((col+1, row))
    # Check west
    if (col > 0 and graph_matrix[row][col-1] == 1):
        neighbors.append((col-1, row))
    return neighbors


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

big_island = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
             [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
             [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
             [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
             [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
             [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
             [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
             [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
             [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

print(island_counter(islands))
print(island_counter(big_island))