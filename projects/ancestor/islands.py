from util import Stack


def island_counter(matrix):
    # create a visited matrix of the same dimentions as the given matrix
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    island_count = 0
    # Walk though each cel of the matrix
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            # Count up the connected componets
            # if it has not been visited
            if not visited[y][x]:
                # When I reach 1 ....
                if matrix[y][x] == 1:
                    # If it has not been visited ....
                    # Do a DFT and marck each 1 as visited
                    visited == dft(x, y, matrix, visited)
                    # increment the counter by 1
                    island_count += 1
                else:
                    visited[y][x] = True


def dft(x, y, matrix, visited):
    '''
    this will mark each connect component as visited
    return visited matrix
    '''
    # create  Stack
    s = Stack()
    # push the starting node onto the stack
    s.push((x, y))
    # While the stack is not Empty
    while s.size() > 0:
        # Pop vertex from top of the stack
        v = s.pop()
        x = v[0]
        y = v[1]
        # check if it's visited. if not ....
        if not visited[y][x]:
            # Mark as visited
            visited[y][x] = True
            # Push each neighbor onto the top of the stack
            for neighbor in get_neighbors((x, y), matrix):  # STUB
                s.push(neighbor)
    return visited


def get_neighbors(vertex, graph_matrix):
    x = vertex[0]
    y = vertex[1]
    neighbors = []
    # check north
    if y > 0 and graph_matrix[x][y-1] == 1:
        neighbors.append((x, y-1))
    # check south
    if y < len(graph_matrix-1) and graph_matrix[x][y+1] == 1:
        neighbors.append((x, y+1))
    # check east
    if x < len(graph_matrix-1) and graph_matrix[x+1][y] == 1:
        neighbors.append((x+1, y))
    # check west
    if x > 0 and graph_matrix[x-1][y] == 1:
        neighbors.append((x-1, y))
    # return all directrions that contain a 1


islands = [[0, 1, 0, 1, 0], [1, 1, 0, 1, 1], [
    0, 0, 1, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
