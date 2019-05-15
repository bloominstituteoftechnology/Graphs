'''
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4
'''

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

# def island_counter(arr):
#     columns = []
#     for i in range(0, len(arr)):
#         for row in arr:
#             columns.append(row[i])
    


# island_counter(islands)

'''
1.) Translate this problem like a Graph Problem
- Islands == Connected components, provide all the groups of connected components.

Plan:
Visit each item in our array, when we get to a 1 figure out if there are connected components. Do a Traversal. Add to an incrementer 

'''

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

def get_neighbors(vertex, matrix):
    x = vertex[0]
    y = vertex[1]
    neighbors = []
    #check north
    if y > 0 and matrix[y-1][x] == 1:
        neighbors.append((x, y-1))
    #check south
    if y < len(matrix) - 1 and matrix[y+1][x] ==1:
        neighbors.append((x, y+1))
    if x < len(matrix[0]) -1 and matrix[y][x+1] == 1:
        neighbors.append((x+1, y))
    if x >0 and matrix[y][x-1] == 1:
        neighbors.append((x-1, y))
    return neighbors



def dft(x, y, matrix, visited):
    s = Stack()
    s.push((x,y))
    while s.size() > 0:
        v = s.pop()
        x =v[0]
        y = v[1]
        if not visited[v[1]][v[0]]:
            visited[y][x] = True
            for neighbor in get_neighbors((x,y), matrix):
                s.push(neighbor)
    return visited


def island_counter(matrix):
    # Create a visited Matrix
    visited = []
    island_count = 0
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    # Walk through each cell in the matrix
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            #if it has not been visited 
            if not visited[y][x]:
                #if it equals One
                if matrix[y][x] == 1:
                    #do a DFT and mark as visited
                    visited = dft(x,y, matrix, visited)
                    #increment count
                    island_count += 1

    return island_count
               
print(island_counter(islands))