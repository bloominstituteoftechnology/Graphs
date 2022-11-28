"""
Write a function that takes a 2D binary array and returns the number of 1 islands
an island consists of 1s that are connected to the north, south, east or west for example:

islands = [[0, 1, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 1, 0, 0], [1, 0, 1, 0, 0], [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4
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


def get_neighbors(current_vertex, matrix):
    neighbors = set()
    row = current_vertex[0]
    col = current_vertex[1]
    # check north direction
    if row > 0 and matrix[row - 1][col] == 1:
        neighbors.add((row-1, col))
    # check south
    if row < len(matrix) - 1 and matrix[row + 1][col] == 1:
        neighbors.add((row+1, col))
    # check west direction
    if col > 0 and matrix[row][col - 1] == 1:
        neighbors.add((row, col-1))
    # check east
    if col < len(matrix) - 1 and matrix[row][col + 1] == 1:
        neighbors.add((row, col + 1))

    return neighbors


def dft(row_index, col_index, matrix, visited_verticies):
    # traverse the 'graph' starting at row_i and col_i
    neighbors_to_visit = Stack()
    neighbors_to_visit.push((row_index, col_index))

    while neighbors_to_visit.size() > 0:
        # pop the first vertex on stack off
        current_vertex = neighbors_to_visit.pop()
        # check if it hasnt been visited yet
        if current_vertex not in visited_verticies:
            # push all neighbors up to stack
            visited_verticies.add(current_vertex)
            for neighbor in get_neighbors(current_vertex, matrix):
                neighbors_to_visit.push(neighbor)
            # mark as visited
            # go to its neighbors
    return visited_verticies


def island_counter(matrix):
    island_count = 0
    # keep track of visited verticies
    visited_verticies = set()
    # go through the matrix of island data
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            # have we seen whats at matrix[island_index][col_index]
            if (row_index, col_index) not in visited_verticies and matrix[row_index][col_index] == 1:
                visited_verticies = dft(
                    row_index, col_index, matrix, visited_verticies)
            # if we see a 1, and its not visited
                island_count += 1
                # do a DFT / BFT
                # keep marking each visited vertex as visited
                # once DFT is done, add 1 to our island count
    return island_count


# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]

islands = [[0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0],
           [1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1],
           [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
           [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0]]

print(island_counter(islands))
