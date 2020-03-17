
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
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        #had 2 add if statement cause it was overriding lines 38-41
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        #Parent to Child relationship add DIRECTED EDGES
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("vertex does not exist")


# Ancestors: [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
def earliest_ancestor(ancestors, starting_node):
    #build our graph
    graph = Graph()
    
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        graph.add_vertex(parent)
        graph.add_vertex(child)
        #directed graph so child -> parent -> grandparent -> ect
        #bfs should also be easier in this case
        graph.add_edge(child, parent)

    #BFS cause 10 will be the last thing it looks at since its the last level
    # If input has no parents return -1
    #edge case what if input node is 8? should return smaller one (per spec) 4!!
    #what if in put is 11(no parents)? should return -1
    queue = Queue()
    queue.enqueue([starting_node])

    longest_path_length = 1
    earliest_ancestor = -1

    #[6 , 3 , 1 , 10]
    while queue.size() > 0:
        path = queue.dequeue()
        # last person
        current_node = path[-1]

        #edge case if input is 8 you have 11/4 as ancestors and spec wants the smaller version
        # OR keeps track of longest path.. should be 4 (6,3,1,10) and return -1 if input is 11 ( doesnt have a parent)
        if (len(path) >= longest_path_length and current_node < earliest_ancestor) or len(path) > longest_path_length:
            longest_path_length = len(path)
            earliest_ancestor = current_node

        neighbors = graph.vertices[current_node]
        for ancestor in neighbors:
            path_copy = list(path)
            path_copy.append(ancestor)
            queue.enqueue(path_copy)
    print(ancestors)
    return earliest_ancestor
