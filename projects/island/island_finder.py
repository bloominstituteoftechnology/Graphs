from util import Stack
'''
Write a function that takes a 2D binary array and returns the number of 1 islands
An island consists of 1s that are connected to the north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 0, 0]]

island_counter(islands) returns 4
'''


def get_neighbors(current_vert, matrix):
    neighbors = set()
    row = current_vert[0]
    col = current_vert[1]
    # check north direction
    if row > 0 and matrix[row - 1][col] == 1:
        neighbors.add((row - 1, col))
    # check south direction
    if row < len(matrix) - 1 and matrix[row+1][col] == 1:
        neighbors.add((row + 1, col))
    # check east direction
    if col < len(matrix[row]) - 1 and matrix[row][col + 1] == 1:
        neighbors.add((row, col + 1))
    # check west direction
    if col > 0 and matrix[row][col - 1] == 1:
        neighbors.add((row, col - 1))

    return neighbors


def dft(row_i, col_i, matrix, visited):
    # traverse the 'graph' starting at row_i and col_i
    neighbors_to_visit = Stack()
    neighbors_to_visit.push((row_i, col_i))

    while neighbors_to_visit.size() > 0:
        # pop  off first vertex
        current_vert = neighbors_to_visit.pop()
        # check if visited
        if current_vert not in visited:
            # mark visited
            visited.add(current_vert)
            # push neighbors up to stack
            for neighbor in get_neighbors(current_vert, matrix):
                neighbors_to_visit.push(neighbor)
    return visited


def island_counter(matrix):
    island_count = 0
    visited = set()
    # keep track of visited verticies
    # go through matrix of island data
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            if (row_index, col_index) not in visited and matrix[row_index][col_index] == 1:
                visited = dft(row_index, col_index, matrix, visited)
                island_count += 1

    # if we see a 1, and it has not been visited
        # -- BFT OR DFT
            # -- Mark each visited vertex as visited
        # -- once traversal is done, increase island count
    return island_count


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

print(island_counter(islands))

# Figure out what the vertices are
# -- vertices are 1s
# Figure out what the edges are
# -- edges are 1s adjacent to eachother in n, s, e, w
# How do we build the graph?
# -- Take input, find vertices
# -- have a plan to find neighbors
# Traverse the graph
