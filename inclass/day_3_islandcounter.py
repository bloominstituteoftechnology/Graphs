islands = [[0, 1, 0, 1, 0],  # 4 islands
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

"""
Example visited matrix: 
​
visited = [[False, True,  False, False, False],
           [True,  True,  False, False, False],
           [False, False, False, False, False],
           [False, False, False, False, False],
           [False, False, False, False, False]]
"""
"""
For each node:
    if node not visited and the node is "land":
        traverse from that node
        increment counter
"""
islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],  # 13 islands
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

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
def get_neighbors(row, col, matrix):
    neighbors = []
    
    # Check north
    if row > 0 and matrix[row-1][col] == 1:
        neighbors.append((row-1, col))
    
    # Check south
    if row < len(matrix) - 1 and matrix[row+1][col] == 1:
        neighbors.append((row+1, col))
    
    # Check west
    if col > 0 and matrix[row][col-1] == 1:
        neighbors.append((row, col-1))
    
    # Check east
    if col < len(matrix[0]) - 1 and matrix[row][col+1] == 1:
        neighbors.append((row, col+1))
        
    return neighbors

def dft(row, col, matrix, visited):
    s = Stack()
    
    s.push( (row, col) )
    
    while s.size() > 0:
        row, col = s.pop()
        
        if not visited[row][col]:
            visited[row][col] = True
            # Above line same as:
            #visited_row = visited[row]
            #visited_row[col] = True 

            for neighbor in get_neighbors(row, col, matrix):
                s.push(neighbor)
                
def island_counter(matrix):  # matrix is a 2D array, AKA list of lists
    island_count = 0
    
    # Create a visited matrix
    visited = []
    
    for _ in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    
    # Walk through each cell in the matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            
            # If it's not visited
            if not visited[row][col]:
                
                # If it's a "1"
                if matrix[row][col] == 1:
                    
                    # Do DFT and mark them as visited
                    dft(row, col, matrix, visited)
                    
                    # increment counter by 1
                    island_count += 1
                    
    # return counter
    return island_count

print(island_counter(islands))  # 4