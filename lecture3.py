islands = [
    [0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0]
]


def island_counter(islands):
    # create a way to keep track of visited nodes
    visited = []
    for _ in range(len(islands)):
        new_row = [False] * len(islands[0])
        visited.append(new_row)

    # print(visited)

    island_count = 0
    # walk through each
    for row in range(len(islands)):
        for col in range(len(islands[0])):
            # if it is not visited
            if not visited[row][col]:
                # if its a 1:
                if islands[row][col] == 1:
                 # do a traversal
                    dft(row, col, islands, visited)
                # increment the counter
                    island_count += 1
    return island_count


def dft(row, col, islands, visited):
    s = []

    s.append((row, col))

    while len(s) > 0:
        v = s.pop()
        row, col = v
        if not visited[row][col]:
            visited[row][col] = True

            for neighbor in get_neighbors(row, col, islands):
                s.append(neighbor)

    # what are the neighbors of (1,3)


def get_neighbors(row, col, islands):
    neighbors = []
    # check north
    if row > 0 and islands[row-1][col] == 1:
        neighbors.append((row-1, col))
    # check south
    if row < len(islands) - 1 and islands[row+1][col] == 1:
        neighbors.append((row+1, col))
        # check west
    if col > 0 and islands[row][col-1] == 1:
        neighbors.append((row, col-1))
    # check east
    if col < len(islands) - 1 and islands[row][col+1] == 1:
        neighbors.append((row, col+1))

    return neighbors


print(island_counter(islands))  # returns 4


"""
When is DFS better?
    - might find the longest path
    - if you suspect the target is deep within the graph
    - if the target node is a leaf
    - can be implemented recursively, or randomly

When is BFS better?
    - might find the shortest path

"""
