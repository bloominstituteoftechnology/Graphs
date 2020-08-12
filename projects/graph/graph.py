

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


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("No vertex exists")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    # Breadth First Traversal
    def bft(self, starting_vertex):

        q = Queue()
        q.enqueue(starting_vertex) # Starting Node
        visited = set()

        while q.size() > 0:
            node = q.dequeue() # First in, First out
 
            if node not in visited:
                visited.add(node)
                print(node)

                # Add neighbors to queue
                for neighbor in self.get_neighbors(node):
                    q.enqueue(neighbor)

        return list(visited)


    # Depth First Traversal (Stack)
    def dft(self, starting_vertex):
        s = Stack()
        s.push(starting_vertex) # Starting Node
        visited = set()

        while s.size() > 0:
            node = s.pop() # Last in First out

            if node not in visited:
                visited.add(node)
                print(node)

                for neighbor in self.get_neighbors(node):
                    if neighbor not in visited:
                        s.push(neighbor)

        return list(visited)


    def dft_recursive(self, starting_vertex, visited = None):
        if visited is None:
            visited = set()

        visited.add(starting_vertex)
        print(starting_vertex)

        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

        return list(visited)


    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            node = path[-1]

            if node not in visited:
                for neighbor in self.get_neighbors(node):
                    if neighbor == destination_vertex:
                        path.append(neighbor)
                        return path
                    else:
                        visited.add(node)
                        current = path.copy()
                        current.append(neighbor)
                        q.enqueue(current)


    def dfs(self, starting_vertex, destination_vertex):
        s = Stack()
        s.push([starting_vertex]) # Starting node 
        visited = set()

        while s.size() > 0:
            node = s.pop()
            last_vertex = node[-1] # End of stack

            if last_vertex not in visited:
                visited.add(last_vertex)

            for neighbor in self.get_neighbors(last_vertex):
                next_path = node[:]
                next_path.append(neighbor)

                if neighbor == destination_vertex:
                    return next_path
                else:
                    s.push(next_path)



    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        if visited == None:
            visited = set()
        if path == None:
            path = [starting_vertex]

        if starting_vertex not in visited:
            visited.add(starting_vertex)

            if starting_vertex == destination_vertex: # Base case
                return path

            for neighbor in self.get_neighbors(starting_vertex):
                result = self.dfs_recursive(neighbor, destination_vertex, visited, path + [neighbor])
                print(result)
                if result:
                    return result
        return None




if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print("Graph Verticies ~",graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("BFT ~", graph.bft(1))

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("DFT ~", graph.dft(1))
    print("DFT recursive ~", graph.dft_recursive(1))

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("BFS ~", graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("DFS ~", graph.dfs(1, 6))
    print("DFS recursive ~", graph.dfs_recursive(1, 6))
