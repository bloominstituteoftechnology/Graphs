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

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

"""
        10
        /
       1   2   4  11
        \ /   / \ /
         3   5   8
          \ / \   \
           6   7   9

        Example input
        6

        1 3
        2 3
        3 6
        5 6
        5 7
        4 5
        4 8
        8 9
        11 8
        10 1
        Example output
        10

        depth first traversal
        so use a stack instead of queue
        pop end of stack

        use hash map to track vertices and their edges
"""
def earliest_ancestor(ancestors, starting_node):
    # Create dict to store vertices and their edges
    rel_map = dict()

    # Create vertices
    vertices = set()
    for vertex in ancestors:
        vertices.add(vertex[0])
        vertices.add(vertex[1])

    # Add them to our map
    for vertex in vertices:
        rel_map[vertex] = set()

    # Add their edges
    for edge in ancestors:
        rel_map[edge[1]].add(edge[0])


    # Now to take the "starting_node", use a depth first traversal stack, the element that gets added to the stack last is the deepest
    # in other words...the oldest ancestor.

    
    result = bft(rel_map, starting_node)
    return result



def bft(rel_map, starting_vertex):
    """
    Print each vertex in breadth-first order
    beginning from starting_vertex.
    """
    s = Stack()
    visited = set()

    s.push(starting_vertex)
    oldest_ancestor = -1
    tie = False

    while s.size() > 0:
        current_vertex = s.pop()

        if current_vertex not in visited:
            visited.add(current_vertex)
            print('current vert', current_vertex)

            neighbors = rel_map[current_vertex]

            if len(neighbors) > 0:
                tie = False
                if len(neighbors) == 2:
                    tie = True

                for neighbor in neighbors:
                    s.push(neighbor)
                    print('stack', s.stack)

                child = s.stack[-1]

    # Exceptions
    if current_vertex == starting_vertex:
        current_vertex = -1
    if tie == True:
        print('current_vertex', current_vertex)
        print('s.stack[-1]', child)
        current_vertex = min(current_vertex, child)

    return current_vertex


# def dft_recursive(rel_map, starting_vertex, stack=None, visited=None, deepest_vertex=None, deepest_traversed=0):
#     """
#     Print each vertex in depth-first order
#     beginning from starting_vertex.
#     This should be done using recursion.
#     """
#     if visited == None and stack == None:
#         visited = set()
#         stack = Stack()
#         visited.add(starting_vertex)
#         stack.push(starting_vertex)
#         deepest_vertex = starting_vertex
    
#     # get neighbors using hashmap
#     neighbors = rel_map[starting_vertex]
    


#     for neighbor in neighbors:
#         if neighbor not in visited:
#             visited.add(starting_vertex)
#             stack.push(neighbor)

#             deepest_traversed += 1
#             deepest_vertex = neighbor

#             print('                   ')
#             print('Depth first traversal stack:', stack.stack)
#             print('deepest_traversed', deepest_traversed)
#             print('deepest_vertex', deepest_vertex)
#             dft_recursive(rel_map, neighbor, stack, visited, deepest_vertex, deepest_traversed)
        

if __name__ == '__main__':
    testing = earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 8)
    print('PLS', testing)