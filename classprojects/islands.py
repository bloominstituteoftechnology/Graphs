islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [1, 1, 0, 1, 1],
           [1, 1, 0, 1, 1],
           [1, 1, 0, 1, 1]]

def island_counter(islands):

visited = set()
island_count = 0
for row in randge(len(islands)):
    for col in range(len(islands[row])):

        if (row, col) not in visted and islands[row] [col] == 1:

            dft(row, col) not in visted and islands[row] [col]
island_counter(islands)