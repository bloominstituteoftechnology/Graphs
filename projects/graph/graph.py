"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
       # """
        #Add a vertex to the graph.

       # """
       self.vertices[vertex]=set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
           self.vertices[v1].add(v2)
        else:
            raise IndexError("cannot create edge based on given vertices ")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #create a queue
        qq = Queue()
        #create a list of visited nodes/vertex
        visited=set()
        #put the starting  node/vertex in the queue
        qq.enqueue(starting_vertex)
        #while queue is not empty
        print()

        while qq.size()>0:
            # pop the starting node of the queue
            vertex = qq.dequeue()
            #if not  visited
            if vertex not in visited:
            #Add in the visited set and mark as visited
                visited.add(vertex)
                print(vertex)
            #get adjacent edges of this vertex and add in the queue
                for next_vert in self.vertices[vertex]:
                    qq.enqueue(next_vert)

            # goto top while loop


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack =  Stack()
        visited=set()
        stack.push(starting_vertex)
        while stack.size()>0:
              vertex=stack.pop()
              if vertex not in visited:
                  visited.add(vertex)
                  print("HERE IS THE VERTICES FOR DFT",vertex)
                  for next_vert in self.vertices[vertex]:
                      stack.push(next_vert)


    def dft_recursive(self, starting_vertex,visited=None):#here we have to add the third parameter
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
       #Adding a 3rd  parameter where we visited
       # we need to have a base case to know what is as default
        if visited is None:
        # then its should be an empty set
           visited=set()

        visited.add(starting_vertex)#we don't need to add the starting vertex in queue but we do need to add iot in the visited
        print("RECURSION", starting_vertex)
        # since we are doing things recursively call itself for each edge, we have sub problem of each problem and wer don't have a queue
        for child_vertex in self.vertices[starting_vertex]:
        #the only thing we care that child vertex should not be  in the visited list
              if child_vertex not in visited:
                  self.dft_recursive(child_vertex,visited)
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        qq= Queue()
        visited=set()
        qq.enqueue([starting_vertex])#we are enqueing in a list so that we could get aii the possible solutions
        while qq.size()>0:
            path= qq.dequeue()
            vertex=path[-1]# last one in the path  is our current vertex
            if vertex not in visited:
                if vertex ==destination_vertex:
                    return path

                visited.add(vertex)
                for next_vert in self.vertices[vertex]:
                    new_path =list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set()
        stack.push([starting_vertex])  # we are enqueing in a list so that we could get aii the possible solutions
        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]  # last one in the path  is our current vertex
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path

                visited.add(vertex)
                for next_vert in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)





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
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

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
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
        
    '''
    print("breadth-firstsearch ")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
