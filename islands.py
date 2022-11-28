"""
Write a function that takes a 2D binary array and returns the number of 1 islands.
 An island consists of 1s that are connected to the north, south, east or west. For example:
​
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
​
islands_seen = [[T, T, F, F, F],
                [F, F, F, F, F],
                [F, F, F, F, F],
                [F, F, F, F, F],
                [F, F, F, F, F]]
​
coords_seen = {(0,0), (0, 1), (0, 2)}
​
island_counter(islands) # returns 4
"""
​
def get_neighbors(row, col, islands):
    # Look Up down left and right for other values of 1
    neighbors = [] # all tuples of coordinates that are neighbors of current (row, col)
​
    # check North
    if row > 0 and islands[row-1][col] == 1:
        neighbors.append( (row-1, col ) )
​
    # check south:
    if row < len(islands) - 1 and islands[row + 1][col] == 1:
        neighbors.append((row + 1, col))
​
    # check west: 
    if col > 0 and islands[row][col-1] == 1:
        neighbors.append((row, col - 1))
​
    if col < len(islands[0]) - 1 and islands[row][col+1] == 1:
        neighbors.append((row, col + 1))
​
    return neighbors
​
def dft(row, col, islands, visited):
    # Do not need to create a new visited set, just use the one
    # from parent function
    # Create a Stack
    stack = [ ( row, col ) ]
​
    while len(stack) > 0:
        # pop the current row/col off the stack
        # check if its visited 
        # if not, flag it as visited, and add neighbors to the stack
        current_vertex = stack.pop()
        current_row = current_vertex[0]
        current_col = current_vertex[1]
​
        if not visited[current_row][current_col]:
            # Flag this vertex as seen
            visited[current_row][current_col] = True
​
            # get neighbors
            for neighbor in get_neighbors(current_row, current_col, islands):
                stack.append(neighbor)
​
​
​
def island_counter(islands):
    # Create some data structure to keep track of 
    visited = []
    for i in range(len(islands)):
        visited.append([False] * len(islands[0]))
​
    island_count = 0
​
    for row in range(len(islands)):
        for col in range(len(islands[0])):
            
            if not visited[row][col]:
                # If I reach a 1
                current_value = islands[row][col]
                if current_value == 1:
                    # Traverse the islands array using BFT/DFT
                    # Flag all adjacent vertices as SEEN so we dont double count them
                    dft(row, col, islands, visited)
                    # Increment the island counter
                    island_count += 1
                else:
                    visited[row][col] = True
    return island_count
​
​
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
​
print(island_counter(islands))