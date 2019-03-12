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
    #   ^ key : ^ value
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

    def __init__(self, graph):
        self.vertices = graph
        # self.vertices = {}

    def add_vertex(self, key):
        self.vertices[key] = set()

    def add_edge(self, key, value):
        # key is the vertex we connecting
        # value is the vertex that we are connecting to
        if not self.vertices[key] and not self.vertices[value]:
            print("error: no vertex exists here")
        else:
            self.vertices.key.add(value)    # directed
            self.vertices[value].add(key)   # undirected/bidirectional

    def add_directed_edge(self, key, value):
        if not self.vertices[key] and not self.vertices[value]:
            raise IndexError("That vertex does not exist")
        else:
            self.vertices[key].add(value)
            # value is the vertex that we are connecting to

    def add_weighted_edge(self):
        pass    # TODO

# You need to have a visited set to keep track of what you have already seen.
# If you did not, in cyclic graphs, you'd just keep looping over and over
    def breadth_first_traversal(self, start_vertex):
        # create a queue for bfs
        queue = []
        queue.append(start_vertex)
        visited = set()
        
        tracker = []  # to return ordered list of nodes
        # sets are chosen because they are faster to index
        # sets cant hold duplicates

        while queue:
            # dequeue a vertex from queue
            for i in self.vertices[queue[0]]:
                if i not in queue and i not in visited:
                    queue.append(i)
            print(f"visited vertex: ", {queue[0]})
            tracker.append(queue[0])
            visited.add(queue.pop(0))

            print(visited)
            print(tracker)

        # put the starting vertex in queue
        # while the queue is not empty:
            # for each key in the graph
            # dequeue the first node from the queue
            # if that node has not been visited
            # mark as visited (we add to set and print at end)
            # then, put all of it's children into the queue


    def depth_first_traversal(self, start_vertex):
        # dft for graphs is very close to bft for graphs
        # the difference is that we use stack in dft and queue in bft
        # this also means we add/remove from the front/index[0] in bft
        # but add/remove to the end in dft
        stack = []  # initialize a queue
        stack.append(start_vertex)

        visited = set()

        tracker = []
        # tracker.append(start_vertex)

        while stack:
            # dequeue a vertex from queue
            current = stack.pop()
            for i in self.vertices[current]:
                if i not in stack and i not in visited:
                    stack.append(i)
            tracker.append(current)
            visited.add(current)

            print(visited)
            print(tracker)

        # while stack:
        #     current = stack.pop()
        #     if current not in visited:
        #         visited.add(current)
        #         tracker.append(current)
        #         print(f"visited vertex: ", {current})
        #         for i in self.vertices[current]: # in keys
        #             stack.append(i)

        #     print(visited)
        #     print(tracker)


g = Graph(graph1)
g.breadth_first_traversal("0")
#g.depth_first_traversal("2")
