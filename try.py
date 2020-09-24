a = [1,2,3]
b = [5,6,7]

c = a
c.append(90)

print(c)
print(a)



matrix = [

        [0, 1, 0, 1, 0],
        [1, 1, 0, 1, 1], 
        [0, 0, 1, 0, 0], 
        [1, 0, 1, 0, 0], 
        [1, 1, 0, 0, 0]
]


from queue import Queue

def check_dir(vert, matrix, i, j, graph):
    if i > 0: # North
        tup = (i-1,j)
        if matrix[i-1][j] == 1 and tup != vert and tup not in graph[vert]:
            graph[vert].add(tup)
            check_dir( vert, matrix, i=i-1, j=j, graph=graph)
    if i < len(matrix)-1: # south
        tup = (i+1,j)
        if matrix[i+1][j] == 1 and tup != vert and tup not in graph[vert]:
            graph[vert].add(tup)
            check_dir( vert, matrix, i+1, j, graph)
    if j < len(matrix[i])-1: # east
        tup = (i,j+1)
        if matrix[i][j+1] == 1 and tup != vert and tup not in graph[vert]:
            graph[vert].add(tup)
            check_dir(vert, matrix, i, j+1, graph)
    if j > 0: # west
        tup = (i,j-1)
        if matrix[i][j-1] == 1 and (i,j-1) !=vert and tup not in  graph[vert]:
            graph[vert].add(tup)
            check_dir( vert, matrix, i, j-1, graph)
    
    return 

# this is the function that will read in the matrix 
# and will form the graph
def form_graph(matrix):
    graph = {}
    myset = set()
    # will loop through the matrix
    for i in range(len(matrix)): # this is doing the rows
        for j in range(len(matrix[i])): # this is the loop that will 
                                        # go through the columns
            if matrix[i][j] == 1:
                # need to put it into the graph 
                graph[(i,j)] = set()
                # add the node to the set
                myset.add((i,j))
                # checking the n, s, e , w
                check_dir((i, j), matrix, i, j, graph)
    return graph



def bft(graph, visited, startNode):
    # will make the bft
    # will use the Queue
    my_queue = Queue()
    my_queue.put(startNode)

    # will now go through the while loop and will deque
    while my_queue.qsize() > 0:
        # dequeuing 
        curNode = my_queue.get()
        if curNode not in visited:
            # adding to the visited
            visited.add(curNode)
            # will loop through the neighbors of the curNode
            for val in graph[curNode]: # this is the set 
                # put it in the queue
                my_queue.put(val) 
    return 1


def find_components(matrix):
    # will call the form graph function
    graph = form_graph(matrix)
    # will now go through and count the components
    m_counter = 0
    visited = set()

    for key in graph:
        if key not in visited:
            m_counter += bft(graph, visited, key)
    return m_counter


print(f"The number of components is: {find_components(matrix)}")


# doing the path
import os

path = os.path.join(os.path.realpath(__file__), "..", "test_line.txt")

print(f"This is the path: {path}")