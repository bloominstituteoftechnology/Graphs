from util import Stack


"""
Connected Components
"""
from util import Stack
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

"""
visited = [[F, T, F, F, F],
           [T, T, F, F, F],
           [F, F, F, F, F],
           [F, F, F, F, F],
           [F, F, F, F, F]]
"""


def island_counter(islands):
    row_count = len(islands)
    col_count = len(islands[0])
    # Create a visited matrix
    visited = []

    for _ in range(row_count):
        visited.append([False] * col_count)

    island_count = 0

    # Walk through each cell of the matrix
    for row in range(row_count):
        for col in range(col_count):

            # If its not been visited
            if not visited[row][col]:
                # If we hit a 1 on the islands
                if islands[row][col] == 1:
                    # Traverse and mark each as visited
                    dft(row, col, islands, visited)

                    # Increment Counter
                    island_count += 1

    return island_count


def dft(row, col, islands, visited):
    s = Stack()

    s.push((row, col))

    while s.size() > 0:
        r, c = s.pop()

        if not visited[r][c]:
            visited[r][c] = True

            for neighbor in get_neighbors(r, c, islands):
                s.push(neighbor)


def get_neighbors(row, col, islands):
    neighbors = []

    row_count = len(islands)
    col_count = len(islands[0])

    # Check North
    if row > 0 and islands[row-1][col] == 1:
        neighbors.append((row-1, col))

    # Check South
    if row < row_count - 1 and islands[row+1][col] == 1:
        neighbors.append((row+1, col))

    # Check West
    if col > 0 and islands[row][col-1] == 1:
        neighbors.append((row, col-1))

    # Check East
    if col < col_count - 1 and islands[row][col+1] == 1:
        neighbors.append((row, col+1))

    return neighbors


print(island_counter(islands))  # returns 4
