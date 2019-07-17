#Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

#island_counter(islands) # returns 4

def count_islands(matrix):
    # make a visited set
    visited = set()
    visited_islands = 0

    # walk across each cell in our matrix
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            cell = matrix[x][y]
            if(x, y) not in visited and cell == 1:
                dft(x, y, visited, matrix)
                visited_islands += 1

    return visited_islands


def dft(x, y, visited, matrix):
    if (x, y) not in visited:
        visited.add((x, y))
        for neighbor in getNeighbors(x, y):
            dft(x, y, visited, matrix)

def getNeighbors(x,y, matrix):
    stepNorth = stepSouth = stepEast = stepWest = False
    neighbors = []

    if ( x > 0):
        stepWest = x -1
    if x < len(matrix[0]) - 1:
        stepEast = x + 1
    if y > 0:
        stepNorth = y - 1
    if y < len(matrix) - 1:
        stepSouth = y + 1

    if stepNorth is not False:
        node = matrix[x][stepNorth]
        if node == 1:
            neighbors.append(node)

    if stepSouth is not False:
        node = matrix[][]
        if node == 1:
            neighbors.append(node)

count_islands(islands)
print(f"Len of islands: {len(islands)}")