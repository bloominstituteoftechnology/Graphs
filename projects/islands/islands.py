from util import Queue
'''
Write a function that takes a 2D binary array and returns the number of 1 islands.
An island consists of 1s that are connected to the north, south, east or west. For example:
'''
# Unweighted
# Undirected
# Cyclic

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

big_islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
               [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
               [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
               [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
               [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
               [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
               [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
               [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
               [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
               [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LindedList:
    def __init__(self, head)
        self.head = head
        self.tail = head

def get_neighbors(vertex, graph_matrix):
    x = vertex[0]
    y = vertex[1]
    neighbors = []
    # Check if there is a 1 to the north
    if y > 0 and graph_matrix[y - 1][x] == 1:
        neighbors.append((x, y-1))
    # Check south
    if y < len(graph_matrix) - 1 and graph_matrix[y + 1][x] == 1:
        neighbors.append((x, y+1))
    # Check east
    if x < len(graph_matrix[0]) - 1 and graph_matrix[y][x + 1] == 1:
        neighbors.append((x + 1, y))
    # Check west
    if x > 0 and graph_matrix[y][x - 1] == 1:
        neighbors.append((x - 1, y))
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
    # Create a visited matrix
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    # Create a counter initialize it to 0
    counter = 0
    # walk through each cell in the original matrix
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            # If it has not been visited
            if not visited[y][x]:
                # When you come across a 1,
                if matrix[y][x] == 1:
                    # DFT it and mark all the connected nodes as visited
                    visited = bft(x, y, matrix, visited)  #STUB
                    # increment counter by 1
                    counter += 1
    return counter

print('Small islands')
print(island_counter(islands))
print('Big islands')
print(island_counter(big_islands))
