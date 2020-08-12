# projects\social\islands.py

# Write a function that takes a 2D binary array and returns the number of 1 islands.
#  An island consists of 1s that are connected to the north, south, east or west.
#  For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]


import sys
sys.path.append(r"C:\Users\Samuel\repos\Graphs\projects\graph")

from util import Stack

def get_neighbors(row, col, matrix):
    neighbors = []

    # Check north
    if row > 0 and matrix[row - 1][col] == 1:
        neighbors.append((row - 1, col))

    # Check south
    if row < len(matrix) - 1 and matrix


# def dft(row, col, matrix, visited):
#     s = Stack()

#     s.push((row, col))

#     while s.size() > 0:
#         v = s.pop()
#         row, col = v

#         if not visited[row][col]:
#             visited[row][col] = True

#             for neighbor in get_neighbors(row, col, matrix):
#                 s.push(neighbor)

def island_counter(matrix):
    visited = []
    for row in range(len(matrix)):
        visited.append([False] * len(matrix[0]))

    island_count = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if not visited[row][col]:
                if matrix[row][col] == 1:
                    dft(row, col, matrix, visited)

                    island_count += 1

    return island_count


print(island_counter(islands))