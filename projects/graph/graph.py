"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from typing import Optional, NoReturn, List, Dict
from collections import defaultdict

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.adj_matrix = [[0 for _ in self.vertices]
                           for _ in self.vertices]

    def vert_not_exists_error(self, v: int) -> Optional[NoReturn]:
        """
        show an error to the screen if vertex does not exist
        """
        try:
            assert v in self.vertices.keys()
        except AssertionError:
            raise Exception(f"Vertex {v} does not exist")
        else:
            return None

    @property
    def adj_matrix_(self):
        """

        """
        return self.adj_matrix

    #@adj_matrix_.setter
    #def adj_matrix_(self):
    #    """ should run every time a new vert is added"""
    #    for row in self.adj_matrix:
    #        row.append(0)
    #    self.adj_matrix.append([0] * len(self.adj_matrix)+1)
    #    pass

    def add_vertex(self, vertex: int):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
        pass

    def add_edge(self, v1: int, v2: int):
        """
        Add a directed edge to the graph.
        """
        self.vert_not_exists_error(v1)
        self.vert_not_exists_error(v2)

        self.vertices[v1].add(v2)
        pass

    def add_undirected_edge(self, v1: int, v2: int):
        """
        add an undirected edge
        """
        self.vert_not_exists_error(v1)
        self.vert_not_exists_error(v2)

        self.vertices[v1].add(v2)
        self.vertices[v2].add(v1)
        pass

    def bft(self, starting_vertex: str):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        ## BFT Psueodcode
        ## create a queue
        qq = Queue()
        # create a list of visited nodes
        visited = set()
        # init order
        order = list()
        # put starting node in queue
        qq.enqueue(starting_vertex)
        # while queeu not empty
        while qq.size() > 0:
            # pop first node out of queue
            vertex = qq.dequeue()
            # if not visited:
            if not vertex in visited:
                # mark as visited
                visited.add(vertex)
                order.append(vertex)
                # get adjacent edges...
                for next_vert in self.vertices[vertex]:
                    # ...and add to list
                    qq.enqueue(next_vert)
        return order

        
    def bft_(self, starting_vertex: int) -> List[int]:
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.

        implemented from this https://youtu.be/s-CYnVz-uh4?t=2197
        """
        # initialize all to "unvisited"
        colors = defaultdict(lambda: 'white')
        # mark starting vertex as "visited"
        colors[starting_vertex] = 'blue'
        # init return list
        order = [starting_vertex]

        # init queue
        q = Queue()
        # enqueue starting vertex
        q.enqueue(starting_vertex)

        while q.queue:
            u = q.queue[0]
            for v in self.vertices[u]:
                if colors[v] == 'white':
                    colors[v] = 'blue'
                    order.append(v)
                    q.enqueue(v)

            q.dequeue()
            colors[u] = 'black'

        return order

    def dft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        ## create a queue
        stack = Stack()
        # create a list of visited nodes
        visited = set()
        # init list of visit order
        order = list()
        # put starting node in queue
        stack.push(starting_vertex)
        # while queeu not empty
        while stack.size() > 0:
            # pop first node out of queue
            vertex = stack.pop()
            # if not visited:
            if not vertex in visited:
                # mark as visited
                visited.add(vertex)
                order.append(vertex)
                # get adjacent edges...
                for next_vert in self.vertices[vertex]:
                    # ...and add to list
                    stack.push(next_vert)

        return order

    def dft_(self, starting_vertex: int) -> List[int]:
        """
        Print each vertex in depth-first order
        beginning from starting_vertex, nonrecursively.
        """
        pass # TODO

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.

        implemented from this https://github.com/quinn-dougherty/Graphs/tree/master/objectives/depth-first-search#pseudocode-for-dfs
        """
        order = list()

        # initialize all to "unvisited"
        colors = defaultdict(lambda: 'white')
        parents = defaultdict()

        def dft_visit(v: int) -> None:
            """ recursion """
            nonlocal order
            # mark that v is now "visitied"
            colors[v] = 'blue'
            order.append(v)
            for neighbor in self.vertices[v]:
                if colors[neighbor]=='white':
                    #order.append(neighbor)
                    parents[neighbor] = v

                    dft_visit(neighbor)
            pass

        dft_visit(starting_vertex)

        return order

    def bfs(self, starting_vertex: int, destination_vertex: int) -> Optional[List[int]]:
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        traversal = self.bft(starting_vertex)
        if destination_vertex in traversal:
            return traversal[:traversal.index(destination_vertex)+1]
        else:
            return None

    def bfs2(self, starting_vertex: int, destination_vertex: int):
        """ step 1: do bft.
            step 2: get path from bft.

            https://www.eecs.yorku.ca/course_archive/2006-07/W/2011/Notes/BFS_part2.pdf
        """
        def get_pred_bft(starting_vertex: int) -> Dict[int, int]:
            flag = defaultdict(bool)
            pred = defaultdict(lambda: None)
            qq = Queue()
            flag[starting_vertex] = True
            qq.enqueue(starting_vertex)
            while qq.queue:
                v = qq.dequeue()
                for w in self.vertices[v]:
                    if not flag[w]:
                        flag[w] = True
                        pred[w] = v
                        qq.enqueue(w)

            return pred

        predecessors = get_pred_bft(starting_vertex)

        path = [destination_vertex]
        key = destination_vertex
        while key in predecessors.keys():
            nxt = predecessors[key]
            path.append(nxt)
            key = nxt

        return path[::-1]

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        traversal = self.dft(starting_vertex)
        # recursive version gives incorrect output
        #traversal = self.dft_recursive(starting_vertex)
        #
        if destination_vertex in traversal:
            return traversal[:traversal.index(destination_vertex)+1]
        else:
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
    print("bft traversal order: ", graph.bft(1))

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("dft traversal order: ", graph.dft(1))

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("dft recursive traversal order: ", graph.dft_recursive(1))

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("bfs path from 1 to 6", graph.bfs2(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("dfs path from 1 to 6: ", graph.dfs(1, 6))

    #print(f"bfs2: {graph.bfs2(1,6)}")
    #graph.bfs2(1,6)
