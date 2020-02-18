# Write a function that takes a 2D binary array and returns 
# the number of 1 islands. An island consists of 1s that are 
# connected to the north, south, east or west. For example:

# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]

# island_counter(islands) # returns 4
# islands[0][4] - 0 refers to first row (y axis); 
# 4 refers to index of fifth item in that list(x axis)
# island_list = islands[0]
# island_list[4] --> [1, 1, 0, 0, 0]
# island_list[4][0] --> 1 

# UNDERSTAND: Translate the problem into graph terminology
    # -each value is a node 
    # -connected nodes are 1's 
    # -edges are adjacent 1's
    # -this is an UNdirected graph 
    # -this is cyclic
    # -island refers to connected components
    # -count up connected nodes and return count

# PLAN:
    # HIGH LEVEL:
        # 2. Build your graph
        # 3. Traverse your graph
    # ALG OVERVIEW:
        # Loop through islands,
        # Do BFS on them and count num times BFS occurs 

# EXECUTE:

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

def get_neighbors(x, y, matrix):
    neighbors = []
    if x > 0 and matrix[y][x - 1] == 1:
        neighbors.append((x - 1, y))
    if x < len(matrix[0]) - 1 and matrix[y][x + 1] == 1:
        neighbors.append((x + 1, y))
    if y > 0 and matrix[y - 1][x] == 1:
        neighbors.append((x, y - 1))
    if y < len(matrix) - 1 and matrix[y + 1][x] == 1:
        neighbors.append((x, y + 1))
    return neighbors

def dfs(x, y, matrix, visited):
    s = Stack()
    s.push((x, y))
    while s.size() > 0:
        v = s.pop()
        if not visited[v[1]][v[0]]:
            visited[v[1]][v[0]] = True
            for neighbor in get_neighbors(v[0], v[1], matrix):
                s.push(neighbor)
    return visited

def island_counter(matrix):
    # Create visited matrix filled with Falses
    visited = []
    for i in range(len(matrix)):  # len of matrix is # of rows(5)
        visited.append([False] * len(matrix[0]))
    # Create counter and initialize to 0
    island_counter = 0
    # Walk through each cell in original matrix    
    for x in range(len(matrix[0])):  # go through columns
        for y in range(len(matrix)):  # go through rows
            # If it hasn't been visited:
            if not visited[y][x]:
                # If you reach a 1
                if matrix[y][x] == 1:
                    # Do BFT and mark each 1 as visited
                    visited = bft(x, y, matrix, visited)
                    # increment counter by 1
                    island_counter += 1
    return island_counter

# def island_counter(matrix):
#     visited = []
#     for i in range(len(matrix)):
#         visited.append([False] * len(matrix[0]))
#     island_count = 0
#     for x in range(len(matrix[0])):
#         for y in range(len(matrix)):
#             if not visited[y][x]:
#                 if matrix[y][x] == 1:
#                     visited = dfs(x, y, matrix, visited)
#                     island_count += 1
#                 else:
#                     visited[y][x] = True
#     return island_count

def print_matrix(matrix):
    for row in matrix:
        print("".join([str(i) for i in row]))

matrix = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 1, 0, 1], [0, 0, 1, 0, 0, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 1, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 1, 0, 0, 0], [1, 0, 1, 1, 0, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]
print_matrix(matrix)
island_counter(matrix)