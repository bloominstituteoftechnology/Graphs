# Write a function that takes a 2D binary array and returns the number of 1
# islands. An island consists of 1s that are connected to the north, south, east
# or west. For example:

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

islands2 = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

def island_counter(islands):
    # Create a way to keep track of visited nodes
    visited = []
    for _ in range(len(islands)):
        new_row = [False] * len(islands[0])
        visited.append(new_row)

    island_count = 0

    # Walk through each cell in the grid

    for row in range(len(islands)):
        for col in range(len(islands[0])):
            # If it's not visited
            if not visited[row][col]:
                # If it's a 1:
                if islands[row][col] == 1:
                    # Do a traversal
                    dft(row, col, islands, visited)

                    # increment the counter
                    island_count += 1

    return island_count

def dft(row, col, islands, visited):
    s = Stack()

    s.push( (row, col) )

    while s.size() > 0:
        v = s.pop()
        row, col = v

        if not visited[row][col]:
            visited[row][col] = True

            for neighbor in get_neighbors(row, col, islands):
                s.push(neighbor)

def get_neighbors(row, col, islands):
    neighbors = []

    # Check north
    if row > 0 and islands[row-1][col] == 1:
        neighbors.append((row-1, col))

    # Check south
    if row < len(islands) - 1 and islands[row+1][col] == 1:
        neighbors.append((row+1, col))

    # Check west
    if col > 0 and islands[row][col-1] == 1:
        neighbors.append((row, col-1))

    # Check east
    if col < len(islands[0]) - 1 and islands[row][col+1] == 1:
        neighbors.append((row, col+1))

    return neighbors

print(island_counter(islands2))