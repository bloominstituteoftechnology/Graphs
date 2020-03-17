class Queue: #queue day 1 dft
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


    def print_queue(self):
        output = []
        for item in self.queue:
            output.append(item)

        return output

class Graph: #use graph class from day1
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
​
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
​
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("vertex does not exist")

def earliest_ancestor(ancestors, starting_node):
     # Initialize an empty graph
    graph = Graph()

    # Iterate through all ancestors
    print(f'Ancestors: {ancestors}')
    for pair in ancestors:
        print(f'Pair: {pair}')
        # Add both verts 
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        # Add edges (CHILD => PARENT)
        graph.add_edge(pair[1], pair[0])

    # Initialize a QUEUE for BFS
    q = Queue()
    # add starting_node to the Queue
    q.enqueue([starting_node])
    # Initialize variables
    max_path_len = 1 # if you have a starting node you have an initial length of 1
    earliest_ancestor = -1 # ERROR HANDLING: if the starting node does not have a PARENT then we will never update the earliest_ancestor and we want to return -1

    # While the QUEUE is NOT empty
    while q.size() > 0:
        # Initialize PATH
        path = q.dequeue()
        print(f'NEW path: {path}')

        # Get Parent Node
        current_vert = path[-1]
        print(f'current_vert: {current_vert}')

        # - V1 
        # (
        #   Check 1 = current path is longer than the current max_path_length
        #   Check 2 = parent node LESS THAN earliest_ancestor 
        # )
        # OR 
        # Check 3 = current path is longer than the current max_path_length

        # If the path is longer or equal and the value is smaller, or if the path is longer)
        # if (len(path) >= max_path_len and current_vert < earliest_ancestor) or (len(path) > max_path_len):
        #     print(f'** UPDATE **')

        #     # Update earliest_ancestor node
        #     earliest_ancestor = current_vert
        #     # update max_path_length
        #     max_path_len = len(path)

        # - V2 
        if len(path) == max_path_len: 
            if current_vert < earliest_ancestor:
                print(f'** UPDATE: CHECK 1 & 2 **')

                # Update earliest_ancestor node
                earliest_ancestor = current_vert
                # # update max_path_length
                max_path_len = len(path)

        if len(path) > max_path_len:
            print(f'** UPDATE: CHECK 3 **')
            # Update earliest_ancestor node
            earliest_ancestor = current_vert
            # update max_path_length
            max_path_len = len(path)


        # Loop through all neighbors of the PARENT node
        for neighbor in graph.vertices[current_vert]:
            # make a copy of the current pathj
            path_copy = list(path)
            print(f'path_copy: {path_copy}')

            # add current neighbor to path
            path_copy.append(neighbor)
            print(f'path_copy POST appended NEIGHBOR: {path_copy}')

            # add updated path to Queue
            q.enqueue(path_copy)
            print(f'current Queue: {q.print_queue()}')

    print(earliest_ancestor)
    return earliest_ancestor 