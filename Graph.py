class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_edge(self,v1,v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("Error vertex not found")
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
    def bft(self,starting_vertex_id):
        queue = []
        queue.append(starting_vertex_id)
        visited = set()
        while len(queue) > 0:
            current_vertex = queue.pop(0)
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    queue.append(neighbor)
    def dft(self,starting_vertex_id):
        stack = []
        stack.append(starting_vertex_id)
        visited = set()
        while len(stack) > 0:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    stack.append(neighbor)
    def bfs(self, starting_vertex_id, target_vertex_id):
        #create an empty queue and Add a PATH TO stating vertex_id
        #I.e add array [1] to the queue
        #create visited set (its empty for now)
        #while queue is not empty:
            #dequeue the current PATH from the queue

            #get the current vertex to analyze from the path
            #use the vertex at the END of the path array
            #if vertext not visited:
                #add vertex to the visited list

                #CHECK IF CURRENT_VERTEX IS THE TARGET_VERTEX
                    #we found the vertex and the path to it
                    #return PATH
                #for each neighbors of current_vertex
                    #ADD the path to that neighbor, to the queue
                        #COPY THE CURRENT PATH
                        #add neighbor to the new path
                        #add the whole path to the queue
our_graph = Graph()

our_graph.add_vertex(1)
our_graph.add_vertex(2)
our_graph.add_vertex(3)
our_graph.add_vertex(4)
our_graph.add_vertex(5)
our_graph.add_vertex(6)
our_graph.add_vertex(7)

our_graph.add_edge(1,2)
our_graph.add_edge(2,3)
our_graph.add_edge(2,4)
our_graph.add_edge(3,5)
our_graph.add_edge(4,6)
our_graph.add_edge(4,7)
our_graph.add_edge(5,3)
our_graph.add_edge(6,3)
our_graph.add_edge(7,6)
our_graph.add_edge(7,1)


# print(our_graph.vertices)
# print(our_graph.get_neighbors(2))
# print(our_graph.bft(1))
print(our_graph.dft(1))