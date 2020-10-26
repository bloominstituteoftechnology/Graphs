from util import Stack
class Graph:

  def __init__(self):
    self.vertices ={}

  def add_vertex(self,vertex):
    self.vertices[vertex] = set()

  def add_edge(self, v1, v2):
    if v1 in self.vertices and v2 in self.vertices:
      self.vertices[v1].add(v2)

  def get_neighbors(self, starting_vertex):
    if starting_vertex in self.vertices:
      return self.vertices[starting_vertex]
  
  def bft(self, starting_vertex):
    queue = []
    queue.append(starting_vertex)
    visited = set()
    
    while len(queue) > 0:
      current_vertex = queue.pop(0)

      if current_vertex not in visited:
        print(f'The current vertex is at {current_vertex}')
        visited.add(current_vertex)

        for neighbor in self.get_neighbors(current_vertex):
          queue.append(neighbor)

    print(f'At the end visited list:{visited}')
    return None   

  def dft(self, starting_vertex):
    stack= Stack()
    stack.push(starting_vertex)
    visited = set()
    print(f'visited before loop:{visited}')

    while stack.size() > 0:
      current_vertex = stack.pop()     

      if current_vertex not in visited:
        print(f'The current vertex is at: {current_vertex}')
        visited.add(current_vertex)    

        for neighbor in self.get_neighbors(current_vertex):
          if neighbor:
            stack.push(neighbor)
            print(f'neighbor is:{neighbor}')

    print(f'visited before loop:{visited}')
    return None   

  def bfs(self, starting_vertex, destination_vertex):
    queue = []
    queue.append([starting_vertex])
    visited = set()

    while len(queue)>0:
      current_path = queue.pop(0)
      current_vertex = current_path[-1] 

      if current_vertex not in visited:
        print(f'The current_vertex is at:{current_vertex}')
        visited.add(current_vertex)

        if current_vertex == destination_vertex:
          print(f'the bsf path:{current_path}')
          return current_path

        for neighbor in self.get_neighbors(current_vertex):
          current_path_copy = list(current_path)
          current_path_copy.append(neighbor)
          queue.append(current_path_copy)
    print(f'current path:{current_path}')
    return None

  def dfs(self, starting_vertex, destination_vertex):
    stack = []
    stack.append([starting_vertex])  
    visited = set()

    while len(stack) > 0:
      current_path = stack.pop()
      current_vertex = current_path[-1]

      if current_vertex not in visited:
        # print(f'The current vertex is at:{current_vertex}')
        visited.add(current_vertex)

        if current_vertex == destination_vertex:
          print(f'the current DFS path is now:{current_path}')
          return current_path

        for neighbor in self.get_neighbors(current_vertex):
          current_path_copy = list(current_path)
          current_path_copy.append(neighbor)
          stack.append(current_path_copy)

    return None    

  def dft_recursive(self, starting_vertex, stack=None):

    if not starting_vertex:
      return None

    if stack == None:
      stack = set()

    if starting_vertex not in stack:
      stack.add(starting_vertex)
      for neighbor in self.get_neighbors(starting_vertex):
        self.dft_recursive(neighbor, stack)
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
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
      1, 2, 4, 6, 3, 5, 7
    '''
    print("Executing Depth First Traverse>>>>>>>>>")
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

    print("Executing B-First Traverse>>>>>>>>>")
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("Executing Depth First Recursive>>>>>>>>>")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("Executing BFirst Search>>>>>>>>>")
    print(graph.bfs(1, 6))
    print(graph.bfs(2, 7))


    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("Executing Depth First Search>>>>>>>>>")
    print(graph.dfs(1, 6))





