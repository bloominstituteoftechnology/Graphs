import random
"""
Simple graph implementation compatible with BokehGraph class.
"""
class Node:
    def __init__(self):
        self.neighbors = []
    def addNeighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node)
    def getNeighbors(self):
        return self.neighbors
    def isNeighbor(self, node):
        return node in self.neighbors

# Another, not-so intuitive solution
# class Vertex:
#     def __init__(self, label, component=-1):
#         self.label = str(label)
#         self.component = component
#
#     def __repr__(self):
#         return 'Vertex: ' + self.label

class Queue:
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

class Stack:
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

class Vertex:
    def __init__(self, vertex_id, x=None, y=None, value=None, color=None):
        self.id = int(vertex_id)
        self.x = x
        self.y = y
        self.value = value
        self.color = color
        self.edges = set()
        if self.x is None:
            self.x = 2 * (self.id // 3) + self.id / 10 * (self.id % 3) #So that vertices will not render in a straight line
        if self.y is None:
            self.y = 2 * (self.id % 3) + self.id / 10 * (self.id // 3) #So that vertices will not render in a straight line
        if self.value is None:
            self.value = self.id
        if self.color is None:
            hexValues = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
            colorString = "#"
            for i in range(0, 3):
                colorString += hexValues[random.randint(0,len(hexValues) - 1)]
            self.color = colorString

    # def __repr__(self):
    #     return 'Vertex, id:{} value: {}, connections: {}'.format(self.id, self.value, self.edges)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        # self.components = 0

    def add_vertex(self, vertex_id, value=None): #come back and add code for values...
        if vertex_id in self.vertices:
            raise Exception('Error: adding vertex that already exists')
        #if not set(edges).issubset(self.vertices):
        #    raise Exception('Error: cannot set edges to non-existent vertices')
        self.vertices[vertex_id] = Vertex(vertex_id, value=value) #...here...from five lines up

    def add_edge(self, vertex_1, vertex_2, bidirectional=True):
        if vertex_1 not in self.vertices or vertex_2 not in self.vertices:
            raise IndexError('Error: Verticies to connect not in graph')
        self.vertices[vertex_1].edges.add(vertex_2)
        if bidirectional:
            self.vertices[vertex_2].edges.add(vertex_1)

    def search(self, start, target=None, method='dfs'):
        """Search the graph using BFS or DFS"""
        chosen_data_structure = [start]
        pop_index = 0 if method == 'bfs' else -1
        visited = set([start])

        while chosen_data_structure:
            current = chosen_data_structure.pop(pop_index)
            if current == target:
                break
            visited.add(current)

            chosen_data_structure.extend(self.vertices[current] - visited)
            visited.update(self.vertices[current])

        return visited

    def dft(self, start_vert, visited=[]):
        visited.append(start_vert)
        print(self.vertices[start_vert].id, ': ', self.vertices[start_vert].value)

        for child_vert in self.vertices[start_vert].edges:
            if child_vert not in visited:
                self.dft(child_vert, visited)

    def dft_stack(self, start_vert): #for some reason it travers from right to left, weird
        #create an empty Stack
        stack = Stack()
        # Put starting vert in the stack
        stack.push(start_vert)
        #Declare visited list
        visited = []
        #While stack is not empty...
        while stack.size() > 0:
            # remove the top item from the stack
            v = stack.pop()
            # if popped value hasn't been visited...
            if v not in visited:
                #... print it
                print("{}: {}".format(self.vertices[v].id, self.vertices[v].value))
                #Add visited vertex to list
                visited.append(v)
                #put the children into the stack
                for next_vert in self.vertices[v].edges:
                    stack.push(next_vert)


    def bft(self, starting_vertex_id):
        q = Queue()
        q.enqueue(starting_vertex_id)
        visited = []

        while q.size() > 0:
            v = q.dequeue()
            # if v not visited...
            if v not in visited:
                print(self.vertices[v].id, ": ", self.vertices[v].value)
                visited.append(v) #mark vertex as visited
                for next_vert in self.vertices[v].edges:
                    q.enqueue(next_vert)

    def dfs(self, starting_vertex_id, target_value, visited=[]):
        visited.append(starting_vertex_id)
        if starting_vertex_id == target_value:
            return True

        for child_vert in self.vertices[starting_vertex_id].edges:
            if child_vert not in visited:
                if self.dfs(child_vert, target_value, visited):
                    return True

        return False

    def bfs(self, starting_vertex_id, target_value):
        q = Queue()
        q.enqueue(starting_vertex_id)
        visited = []
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                if self.vertices[v].value == target_value:
                    return True
                visited.append(v)
                for next_vert in self.vertices[v].edges:
                    q.enqueue(next_vert)
        return False

    def dfs_path(self, starting_vertex_id, target_value, visited=[], path=[]):
        visited.append(starting_vertex_id)
        path = path + [starting_vertex_id]
        if self.vertices[starting_vertex_id].value == target_value:
            return path
        for child_vert in self.vertices[starting_vertex_id].edges:
            if child_vert not in visited:
                new_path = self.dfs_path(child_vert, target_value, visited, path)
                if new_path:
                    return new_path

        return None

    def bfs_path(self, starting_vertex_id, target_value):
        q = Queue()
        q.enqueue([starting_vertex_id])
        visited = []
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]
            if v not in visited:
                if self.vertices[v].value == target_value:
                    return path
                visited.append(v)
                for next_vert in self.vertices[v].edges:
                    # q.enqueue(next_vert) is no more
                    new_path = list(path)
                    new_path.append(next_vert)
                    q.enqueue(new_path)
        return None


graph = Graph()
print(graph.vertices)
graph.add_vertex(0, value="Shuri")
graph.add_vertex(1, value="T'Challa!")
graph.add_vertex(2, value="Cap")
graph.add_vertex(3, value="Spidey")
graph.add_vertex(4, value="Tony")
graph.add_vertex(5, value="Thanos")
graph.add_vertex(6, value="The Maw")
graph.add_vertex(7, value="Hulk")
graph.add_vertex(8, value="Thor")
graph.add_vertex(9, value="Erik")
graph.add_vertex(10, value="Nat")
graph.add_vertex(11, value="Vision")
graph.add_vertex(12, value="Wanda")
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 6)
graph.add_edge(3, 7)
graph.add_edge(1, 4)
graph.add_edge(1, 5)
graph.add_edge(4, 8)
graph.add_edge(4, 9)

for vertex, vertex_info in graph.vertices.items():
    print(vertex, ": ", vertex_info.value, ", connected to vertices ", vertex_info.edges)

#print(graph.search('1', method='bfs'))
print('DFT: ')
graph.dft(graph.vertices[0].id)
print('\n DFT using Stack method')
graph.dft_stack(graph.vertices[0].id)
print('\nBFT:')
graph.bft(graph.vertices[0].id)
print('\nDFS:')
print(graph.dfs(graph.vertices[0].id, 9))
print('\nBFS:')
print(graph.bfs(graph.vertices[0].id, "Thanos"))
print('\nDFS Path:')
print(graph.dfs_path(graph.vertices[0].id, "Hulk"))
print('\nBFS Path:')
print(graph.bfs_path(graph.vertices[0].id, "Hulk"))
