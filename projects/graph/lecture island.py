from util import Stack, Queue  # These may come in handy


# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
# island_counter(islands)  # returns 4

bigIslands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
              [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
              [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
              [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
              [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
              [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
              [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
              [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
              [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]
# 13 islands


def islandCounter(matrix):

    visited = set()
    islandCount = 0

    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if (x, y) not in visited:
                if matrix[y][x] == 1:
                    newlyVisited = dft(x, y, matrix, visited)
                    islandCount += 1
                    visited = newlyVisited
                else:
                    visited.add((x, y))
    print(islandCount)


def dft(x, y, matrix, visited):
    s = Stack()
    s.push((x, y))
    newlyVisited = visited
    while s.size() > 0:
        v = s.pop()
        if v not in newlyVisited:
            newlyVisited.add(v)
            for neighbor in getNeighbors(v, matrix):
                s.push(neighbor)
    return newlyVisited

def getNeighbors(vertex, matrix):
    x = vertex[0]
    y = vertex[1]

    neighbors = set()
    # north
    yOffset = y - 1
    if yOffset >= 0 and matrix[yOffset][x] == 1:
        neighbors.add((x, yOffset))
    # south
    yOffset = y + 1
    if yOffset < len(matrix) and matrix[yOffset][x] == 1:
        neighbors.add((x, yOffset))
    # west
    xOffset = x - 1
    if xOffset >= 0 and matrix[y][xOffset] == 1:
        neighbors.add((xOffset, y))
    # east
    xOffset = x + 1
    if xOffset < len(matrix) and matrix[y][xOffset] == 1:
        neighbors.add((xOffset, y))
    return neighbors


# print(dft(1, 0, islands, set( [(0, 0), (1, 0)] )))

# print(getNeighbors((0, 0), islands))

islandCounter(islands)
