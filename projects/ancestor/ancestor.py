# parent child relationship

class Stack():
    def __init__(self):
        self.stack = []
    def __repr__(self):
        return str(self.stack)

    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

#  if key == value there is a generation conection 
vertices = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
def dfs(starting_vertex, destination_vertex):
    """
    Return a list containing a path from
    starting_vertex to destination_vertex in
    depth-first order.
    """
    stack = Stack()
    stack.push([starting_vertex])
    visited = set()
    while stack.size() > 0:
        currrent_path = stack.pop()
        print(f'\nthe currrent_path is {currrent_path}')
        current_node = currrent_path[- 1]
        print(f'\nthe current_node is {current_node}')
        if current_node == destination_vertex:
            return currrent_path
        if current_node not in visited:
                visited.add(current_node)
                print(f'visted: {visited}')
                for neighbor in vertices[current_node]:
                    newPath = list(currrent_path)
                    newPath.append(neighbor)
                    print(f'the new path is: {newPath}')
                    stack.push(newPath)
'''
    10
    /
    1   2   4  11
    \ /   / \ /
    3   5   8
    \ / \   \
    6   7   9
'''
    #Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1
def earliest_ancestor(vertices, starting_node):
    # loop through all vertices
    print(vertices)
    for vert in vertices:
        # print(vert)
        #   There is a generation conection if key == value, parent is child of earlier generation
        # vertices = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
        print(f'the parent is {vert[0]}')
        print(f'the child is {vert[1]}')
        if vert[1] == vert[0]:
            print('here')
            print(vert)

    # use DFS to get the fartherst distance
    # return ancestor that is the farthest distance away and lowest ID, 9's furthest ancester is 4
    # if starting_node has no ancestors
        #  return -1

    search = dfs(starting_node, 1)
    return search

print(earliest_ancestor(vertices, 1))
# graph = Graph()

# graph.add_vertex(1)
# graph.add_vertex(2)
# graph.add_vertex(3)
# graph.add_vertex(4)
# graph.add_vertex(5)
# graph.add_vertex(6)
# graph.add_vertex(7)
# graph.add_vertex(8)
# graph.add_vertex(9)
# graph.add_vertex(10)
# graph.add_vertex(11)
# graph.add_edge(1, 3)
# graph.add_edge(2, 3)
# graph.add_edge(3, 6)
# graph.add_edge(4, 5)
# graph.add_edge(4, 8)
# graph.add_edge(5, 6)
# graph.add_edge(5, 7)
# graph.add_edge(1, 2)
# graph.add_edge(2, 4)
# graph.add_edge(8, 9)
# graph.add_edge(10, 1)
# graph.add_edge(11, 8)
