"""
Remember these steps to solve almost any graphs problem:
- Translate the problem into terminology you've learned this week
- Build your graph
- Traverse your graph


ISLANDS MATRIX CHALLENGE!
--------------------------
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
island_counter(islands) # returns 4
traversal (define a function) => dft(row, col, matrix, visited) => returns visited
get neighbors (define function) => get_nieghbors(col, row, matrix) => check north south east and west for connections / x, y / col / row
each island is a vertex
each connection of north, south, east or west (edge)
"""

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

def dft(row, col, islands, visited):
    s = Stack()
    s.push((row, col))

    while s.size() > 0:
        rw, cl = s.pop()
        if not visited[rw][cl]:
            visited[rw][cl] = True

            for neighbor in get_neighbors(rw, cl, islands):
                s.push(neighbor)


def get_neighbors(row, col, islands):
    neighbors = []

    row_count = len(islands)
    col_count = len(islands[0])

    # Check north
    if row > 0 and islands[row-1][col] == 1:
        neighbors.append((row-1, col))

    # South
    if row < row_count -1 and islands[row+1][col] == 1:
        neighbors.append((row+1, col))
    
    # West
    if col > 0 and islands[row][col-1] == 1:
        neighbors.append((row, col-1))
    
    # East
    if col < col_count -1 and islands[row][col+1] == 1:
        neighbors.append((row, col +1))

    return neighbors

    

def island_counter(matrix):
    # create a visited matrix. list of F for each array
    visited = []

    for _ in range(len(matrix)):
        visited.append([False]* len(islands[0]))
    
    island_count = 0
    
    # walk through each cell of the matrix 
    for row in range(len(matrix)):
        for col in range(len(islands[0])):

        # if not visited
            if not visited[row][col]:
            # if hit a 1 on islands
                if islands[row][col] == 1:
                # traverse and mark each as visited
                    dft(row, col, islands, visited)
                # increment counter
                island_count += 1
    return island_count


if __name__ == "__main__":
    islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

    print(island_counter(islands))  # 4

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

    print(island_counter(islands))  # 13

