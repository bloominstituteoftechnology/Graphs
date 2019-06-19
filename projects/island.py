"""
Write a function that takes a 2D binary array and returns the number of 1
islands. An island consists of 1s that are connected to the north, south,
east or west.
For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4
"""


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)

        return None

    def size(self):
        return len(self.queue)


# Create an empty set to store visited vertices
def bfs(starting_vertex, vertices, islands):
    # Flag to identify finding new node
    bfs_flag = False

    # Create a Queue
    queue = Queue()

    # Add starting vertex
    queue.enqueue(starting_vertex)

    # BFS logic
    while queue.size() > 0:
        vertex = queue.dequeue()

        if vertex not in vertices:
            vertices.add(vertex)

            # Indicates finding a new node
            if islands[vertex[0]][vertex[1]] == 1 and not bfs_flag:
                bfs_flag = True

            for next_vertex in get_neighbours(vertex, islands):
                if next_vertex not in vertices:
                    queue.enqueue(next_vertex)
    return bfs_flag


# Find and return neighbours for each vertex
def get_neighbours(vertex, islands):

    island_rows = len(islands)
    island_cols = len(islands[0])

    neighbours = []

    if vertex[0] != 0:
        if islands[vertex[0]-1][vertex[1]] == 1:
            neighbours.append((vertex[0]-1, vertex[1]))

    if vertex[0] != island_rows-1:
        if islands[vertex[0]+1][vertex[1]] == 1:
            neighbours.append((vertex[0]+1, vertex[1]))

    if vertex[1] != 0:
        if islands[vertex[0]][vertex[1]-1] == 1:
            neighbours.append((vertex[0], vertex[1]-1))

    if vertex[1] != island_cols-1:
        if islands[vertex[0]][vertex[1]+1] == 1:
            neighbours.append((vertex[0], vertex[1]+1))

    return neighbours


def island_counter(islands):
    # Initialize island counter
    counter = 0

    # The set is maintained outside bfs since we need can visit
    # disjoint graph and the information needs to be retained.
    vertices = set()

    island_rows = len(islands)
    island_cols = len(islands[0])

    for i in range(island_rows):
        for j in range(island_cols):
            result = bfs((i, j), vertices, islands)

            if result:
                counter += 1

    return counter


if __name__ == "__main__":
    islands = [[0, 1, 0, 1, 0],
               [1, 1, 0, 1, 1],
               [0, 0, 1, 0, 0],
               [1, 0, 1, 0, 0],
               [1, 1, 0, 0, 0]]

    islands_str = """
                  [[0, 1, 0, 1, 0],
                   [1, 1, 0, 1, 1],
                   [0, 0, 1, 0, 0],
                   [1, 0, 1, 0, 0],
                   [1, 1, 0, 0, 0]]
                  """
    print(islands_str)
    print("Should return count 4")
    print(island_counter(islands))

    islands = [[0, 1, 1, 1, 0],
               [1, 1, 0, 1, 1],
               [0, 0, 1, 0, 0],
               [1, 0, 1, 0, 0],
               [1, 1, 0, 0, 0]]

    islands_str = """
                  [[0, 1, 1, 1, 0],
                   [1, 1, 0, 1, 1],
                   [0, 0, 1, 0, 0],
                   [1, 0, 1, 0, 0],
                   [1, 1, 0, 0, 0]]
                  """
    print(islands_str)
    print("Should return count 3")
    print(island_counter(islands))

    islands = [[0, 1, 1, 1, 0],
               [1, 1, 0, 1, 1],
               [0, 0, 1, 0, 0],
               [1, 0, 1, 0, 0],
               [1, 1, 1, 0, 0]]

    islands_str = """
                  [[0, 1, 1, 1, 0],
                   [1, 1, 0, 1, 1],
                   [0, 0, 1, 0, 0],
                   [1, 0, 1, 0, 0],
                   [1, 1, 1, 0, 0]]
                  """
    print(islands_str)
    print("Should return count 2")
    print(island_counter(islands))

    islands = [[0, 1, 0, 1, 0],
               [1, 1, 0, 1, 1],
               [0, 0, 1, 0, 0],
               [1, 0, 1, 0, 1],
               [1, 1, 0, 0, 0]]

    islands_str = """
                  [[0, 1, 0, 1, 0],
                   [1, 1, 0, 1, 1],
                   [0, 0, 1, 0, 0],
                   [1, 0, 1, 0, 1],
                   [1, 1, 0, 0, 0]]
                  """
    print(islands_str)
    print("Should return count 5")
    print(island_counter(islands))
