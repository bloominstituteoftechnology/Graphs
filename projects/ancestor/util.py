
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

def dfs(self, starting_vertex, destination_vertex):
    """
    Return a list containing a path from
    starting_vertex to destination_vertex in
    depth-first order.
    """
    # Create empty queue and enque path to starting vertex
    stack = Stack()
    stack.push([starting_vertex])
    # [1]
    # Create an empty set to track visited vertices
    visited = set()
    # while the queue is not empty
    while stack.size() > 0:
        # get the current vertex path (deque)
        currrent_path = stack.pop()
        # [1, 2]
        print(f'\nthe currrent_path is {currrent_path}')
        # set the current vertex to the last element of the path
        current_node = currrent_path[- 1]
        print(f'\nthe current_node is {current_node}')
        # [2]
        # check if current vertex is destination
        if current_node == destination_vertex:
            return currrent_path
        # check if current vertex has not been visited
        if current_node not in visited:
            # Mark current vertex as visited
                # Add the current vertex to a visited set
                visited.add(current_node)
                # {1, 2}
                print(f'visted: {visited}')
                # queue up new paths with each neighbor
                for neighbor in self.get_neighbors(current_node):
                    newPath = list(currrent_path)
                    # [1,2, 4]
                    newPath.append(neighbor)
                    # [4]
                    print(f'the new path is: {newPath}')
                    # take current path 
                    stack.push(newPath)
                    # [1, 2, 3, 4]

                    # append neighbor to it's path
                    # queue up new path
def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        while stack.size() > 0:
            node = stack.pop()
            if node not in visited:
                print(node)
                visited.add(node)
                for neighbor in self.get_neighbors(node):
                    stack.push(neighbor)