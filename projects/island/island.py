from util import Stack, Queue

# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]

islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
               [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
               [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
               [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
               [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
               [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
               [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]


#                  (x,y),
def get_neighbors(vertex, graph_matrix):
    x = vertex[0]
    y = vertex[1]
    neighbors = []
    # check north
    if y > 0 and graph_matrix[y-1][x] == 1:
        neighbors.append((x, y-1))
    # check south
    if y < len(graph_matrix)-1 and graph_matrix[y+1][x] == 1:
        neighbors.append((x, y+1))
    # check east
    if x < len(graph_matrix[0])-1 and graph_matrix[y][x+1] == 1:
        neighbors.append((x+1, y))
    # check west
    if x > 0 and graph_matrix[y][x-1] == 1:
        neighbors.append((x-1, y))

    print(neighbors)
    return neighbors


def bft(x, y, matrix, visited):
    q = Queue()
    q.enqueue((x, y))
    while q.size() > 0:
        v = q.dequeue()
        x = v[0]
        y = v[1]
        if not visited[y][x]:
            visited[y][x] = True
            for neighbor in get_neighbors((x, y), matrix):
                q.enqueue(neighbor)

    return visited


def island_counter(matrix):
    visited = []
    for i in range(len(matrix)):
        visited.append([False]*len(matrix[0]))
        # for each row, however many items are in the first row, that is the number of columns we add to visited as placeholders. should looke like this:
        # [[False, False, False, False, False],
        # [False, False, False, False, False],
        # [False, False, False, False, False],
        # [False, False, False, False, False],
        # [False,False, False, False, False]]
    # sanity check:
    print(visited)
    count = 0
    print('looped from matrix')
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if not visited[y][x]:
                if matrix[y][x] == 1:
                    visited = bft(x, y, matrix, visited)
                    count += 1
    return count


print(island_counter(islands))
