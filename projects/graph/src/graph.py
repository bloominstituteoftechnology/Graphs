"""
Simple graph implementation
"""

# field vertices that map vertex labels to edges
# add vertex method
# add edge method

#
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

    def add_vertex(self, key):
        self.vertices[key] = set()

    def add_edge(self, key, value):
        if not self.vertices[key] and not self.vertices[value]:
            print("error: no vertex exists here")
        else:
            self.vertices.key.add(value)    # directed
            self.vertices[value].add(key)   # undirected/bidirectional

    def add_directed_edge(self, key, value):
        if not self.vertices[key] and not self.vertices[value]:
            print("error: no vertex exists here")
        else:
            self.vertices[key].add(value)

    def add_weighted_edge(self):
        pass    # TODO

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
#            print(f"visited vertex: ", {queue[0]})
            tracker.append(queue[0])
            visited.add(queue.pop(0))

            print(visited)
            print(tracker)

    def depth_first_traversal(self, start_vertex):

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

    def depth_first_trav_recursive(self, start_vertex):
        # stack = []
        # stack.append(start_vertex)
        visited = set()

        for i in self.vertices[start_vertex]:
            if i not in visited:
                visited.add(i)
                depth_first_trav_recursive(i, visited)
        return visited

    def breadth_first_search(self):
        # start_vertex
        # target_vertex

        # add to the end, take from the front? QUEUE
        # pop from q

        # for each of the current nodes neighbors
        # make a copy with the neighbor appended to the end

        # change vertex, add copies to queue

        # repeat from for loop
        pass    # TODO
        # keep track of every single path you can traverse to your target
        # one you find your target value
            # print out that path
    
    def depth_first_search(self):
        pass    # TODO




g = Graph(graph3)
# g.breadth_first_traversal("1")
# g.depth_first_traversal("1")
g.depth_first_trav_recursive("1")
