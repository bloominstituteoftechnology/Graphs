"""
Write a function that takes a 2D binary array and returns the number of 1-
islands. An island consists of 1s that are connected to the north, south, east
or west. For example:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
island_counter(islands) # returns 4
"""


def explore_island(islands, island_map, island_no, i, j):

    island_map[(i, j)] = island_no

    # Explore east.
    if i > 0:
        if islands[i - 1][j] == 1 and (i - 1, j) not in island_map:
            explore_island(islands, island_map, island_no, i - 1, j)

    # Explore west.
    if i < len(islands) - 1:
        if islands[i + 1][j] == 1 and (i + 1, j) not in island_map:
            explore_island(islands, island_map, island_no, i + 1, j)

    # Explore north.
    if j > 0:
        if islands[i][j - 1] == 1 and (i, j - 1) not in island_map:
            explore_island(islands, island_map, island_no, i, j - 1)

    # Explore south.
    if j < len(islands[0]) - 1:
        if islands[i][j + 1] == 1 and (i, j + 1) not in island_map:
            explore_island(islands, island_map, island_no, i, j + 1)


def island_counter(islands):
    island_map = {}
    num_islands = 0

    for i in range(len(islands)):
        for j in range(len(islands[0])):
            if islands[i][j] == 1:
                if (i, j) not in island_map:
                    num_islands += 1
                    explore_island(islands, island_map, num_islands, i, j)

    return num_islands


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
print(island_counter(islands))
