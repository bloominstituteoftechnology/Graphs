"""
Simple graph implementation
"""

# field vertices that map vertex labels to edges
# add vertex method
# add edge method

# Brady's Queue class for use in his bft and dft
# comment out later
# class Queue:
#     def __init__(self):
#         self.queue = []
#     def enqueue(self, value):
#         self.queue.append(value)
#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None
#     def size(self):
#         return (len(self.queue))

graph1 = {
    '0': {'1', '3'},
    #   ^ v1 : ^ value
    '1': {'0'},  # inside value is a set, indicated by curly brackets
    '2': set(),  # instantiates an empty set
    '3': {'0'}
}

graph2 = {
    "1": {"5", "2"},
    "2": {"5", "1", "3"},
    "3": {"4", "2"},
    "4": {"3", "6", "5"},
    "5": {"4", "1", "2"},
    "6": {"4"}
}

graph3 = {
    "1": {"2", "3"},
    "2": {"4", "5", "1"},
    "3": {"6", "7", "1"},
    "4": {"2", "8", "9"},
    "5": {"2", "10", "11"},
    "6": {"3", "12", "13"},
    "7": {"3", "14", "15"},
    "8": {"4"},
    "9": {"4"},
    "10": {"5"},
    "11": {"5"},
    "12": {"6"},
    "13": {"6"},
    "14": {"7"},
    "15": {"8"}
}


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        # self.vertices = graph
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        # v1 is the vertex we connecting
        # v2 is the vertex that we are connecting to
        if not self.vertices[v1] and not self.vertices[v2]:
            print("error: no vertex exists here")
        else:
            self.vertices.v1.add(v2)    # directed/one way
            # self.vertices[v2].add(v1)   # undirected/bidirectional

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            # v2 is the vertex that we are connecting to
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def add_weighted_edge(self):
        pass    # TODO
        """ What is a weighted edge? """

# You need to have a visited set to keep track of what you have already seen.
# If you did not, in cyclic graphs, you'd just keep looping over and over
    # breadth_first_traversal
    def bft(self, start_vertex):
        # create a queue for bfs
        queue = []
        queue.append(start_vertex)
        # create a set to store your vertices
        visited = set()
        # create tracker to return ordered list of nodes
        tracker = []  
        # sets are chosen because they are faster to index
        # sets cant hold duplicates
        print(f"bf trav start", start_vertex)
        while queue:
            # dequeue a vertex from queue
            for i in self.vertices[queue[0]]:
                # if i is not in visited:
                if i not in queue and i not in visited:
                    # add to queue
                    queue.append(i)
        #  print(f"visited vertex: ", {queue[0]})
            tracker.append(queue[0])
            visited.add(queue.pop(0))

        print(f"bf trav visited", visited)
        print(f"bf trav tracker", tracker)

        # put the starting vertex in queue
        # while the queue is not empty:
            # for each v1 in the graph
            # dequeue the first node from the queue
            # if that node has not been visited
            # mark as visited (we add to set and print at end)
            # then, put all of it's children into the queue

    # depth_first_traversal
    def dft(self, start_vertex):
        # dft for graphs is very close to bft for graphs
        # the difference is that we use stack in dft and queue in bft
        # this also means we add/remove from the front/index[0] in bft
        # but add/remove to the end in dft
        stack = []  # initialize a stack
        stack.append(start_vertex)
        visited = set()
        tracker = []
        # tracker.append(start_vertex)
        print(f"df trav start", start_vertex)
        while stack:
            # dequeue a vertex from queue
            current = stack.pop()
            for i in self.vertices[current]:
                if i not in stack and i not in visited:
                    stack.append(i)
            tracker.append(current)
            visited.add(current)

        print(f"df trav visited", visited)
        print(f"df trav tracker", tracker)

    # depth_first_traversal_recursive
    def dft_r(self, start_vertex, visited=None):
        # cant set default variables to set/dict/list?
        # mark the start node as visited
        # then call recursive on each unvisited neighbor

        # cant use sets in recursion because we need to maintain
        # its values. It can be done with a helper method.
        # Here we will add another parameter that will be default None
        # but allows the visited set to pass through during recursion unchanged

        if visited is None:
            visited = set()
        visited.add(start_vertex)
        print(f"dftrav-recur visited: {visited}")
        for i in self.vertices[start_vertex]:
            if i not in visited:
                self.dft_r(i, visited)

    # bfs is good for social media, like fb
    # with bfs you need to store all the children
    # breadth_first_search
    def bfs_path(self, start_vertex, end_vertex):
        # keep track of every single path you can traverse to your target
        # one you find your target value
        # print out that path
        queue = []
        queue.append(start_vertex)
        visited = set()

        while queue:
            path = queue.pop(0)
            v = path[-1]  # grabs the last item (not int) from a list
            if v not in visited:
                visited.add(v)
                if v == end_vertex:
                    return path
                for i in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(i)
                    queue.append(new_path)
        return None

    # dfs is good for mazes
    # depth_first_search
    def dfs(self, start_vertex, end_vertex):
        stack = []
        visited = set()
        stack.append(start_vertex)

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                if current == end_vertex:
                    return visited
                for i in self.vertices[current]:
                    # if i not in visited:
                    stack.append(i)
    # comment on reasons why dfs returns an set, not array like BFS

    # depth_first_search_recursive?? Nope
    def dfs_r(self, start_vertex, end_vertex, visited=None):
        stack = []
        stack.append([start_vertex])
        visited = set()
        while stack:
            path = stack.pop()
            v = path[-1]
            if v not in visited:
                if v == end_vertex:
                    return path
                visited.add(v)
                for next_vert in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.append(new_path)
        return None

    def dfs_r_path(self, start_vertex, end_vertex, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(start_vertex)
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        for child_vertex in self.vertices[start_vertex]:
            if child_vertex not in visited:
                new_path = self.dfs_r_path(child_vertex, end_vertex, visited, path)
                if new_path:
                    return new_path
        return None

""" g = Graph(graph3)
print(g.breadth_first_traversal("2"))
print(g.depth_first_traversal("2"))
print(g.depth_first_trav_recursive("2", ))

# find a path
print(g.breadth_first_search("1", "6")) # start, find
print(g.depth_first_search("1", "6")) # start, find """
