"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
        '''
        {
            A:{B},
            B:{C},
            C:{},
            D:{}
        }
        '''

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        '''
        visited (set) - [1, 2, 3, 4, 5, 6, 7] - print
        visited = ([])
        plan_to_visit (queue) - when empty, we are finished
        examine starting vertex for edges, add to [visited](print) -- remove from plan_to_visit
        add edges to [plan_to_visit] if edge not in [visited]
        while plan_to_visit not empty -- visit plan_to_visit[0]

        lecture solution:
        neighbors_to_visit = Queue()
        neighbors_to_visit.enqueue([starting_vertex])
        visited_vertices = set()

        while neighbors_to_visit.size() > 0:
            current_path = neighbors_to_visit.dequeue()
            current_vertex = current_path[-1]
            if current_vertex not in visited_vertices:
                if current_vertex == destination_vertex:
                    return current_path
                visited_vertices.add(current_vertex)
                for neighbor in self.get_neighbors():
                    new_path = list(current_path)
                    new_path.append(neighbor)
                    neighbors_to_visit.enqueue(new_path)

        '''
        # create a plan_to_visit queue and add starting_vertex to it
        plan_to_visit = Queue()
        plan_to_visit.enqueue(starting_vertex)
        # create a Set for visited
        visited_vertices = set()
        # while the plan_to_visit queue is not Empty:
        while plan_to_visit.size() > 0:
            # dequeue the first vertex on the queue
            current_vertex = plan_to_visit.dequeue()
            # if it has not been visited
            if current_vertex not in visited_vertices:
                # print vertex
                print(current_vertex)
                # mark it as visited, add to visited
                visited_vertices.add(current_vertex)
                # add all neighbors to queue
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack plan_to_visit
        # create a set visited
        plan_to_visit = Stack()
        plan_to_visit.push(starting_vertex)
        visited_vertices = set()
        while plan_to_visit.size() > 0:
            current_vertex = plan_to_visit.pop()
            if current_vertex not in visited_vertices:
                print(current_vertex)
                visited_vertices.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.push(neighbor)

    def dft_recursive(self, start_vert, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(start_vert)
        print(start_vert)
        for child_vert in self.vertices[start_vert]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue a PATH to the starting vertex
        # queue.enqueue([starting_vertex])
        # create a set for visited vertices
        # while the queue is not empty
        #  dequeue the first PATH
        # grab the last vertex in the path
        # if it hasn't been visited
        # check if it is target
        # return path
        # mark it as visited
        # make new versions of current path for each neighbor queue[[1, 2, 3], [1, 2, 4]]
        # duplicate the path
        # add the neighbor
        # add new path to the queue

        paths = Queue()
        paths.enqueue([starting_vertex])

        visited = set()

        while paths.size() > 0:
            current_path = paths.dequeue()
            current_place = current_path[(len(current_path) - 1)]
            if current_place not in visited:

                visited.add(current_place)

                if current_place == destination_vertex:
                    return current_path
            for neighbor in self.get_neighbors(current_place):
                # print(current_place, neighbor, current_path)
                new_path = list(current_path)
                new_path.append(neighbor)
                # print(new_path)
                paths.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        paths = Stack()
        paths.push([starting_vertex])

        visited = set()

        while paths.size() > 0:
            current_path = paths.pop()
            current_place = current_path[(len(current_path) - 1)]

            if current_place not in visited:
                visited.add(current_place)

                if current_place == destination_vertex:
                    return current_path

                for neighbor in self.get_neighbors(current_place):
                    new_path = list(current_path)
                    new_path.append(neighbor)
                    paths.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        for child_vert in self.get_neighbors(starting_vertex):
            if child_vert not in visited:
                new_path = self.dfs_recursive(
                    child_vert, destination_vertex, visited, path)
                if new_path:
                    return new_path
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
    print('BFT')
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('DFT')
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('BFS')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('DFS')
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
