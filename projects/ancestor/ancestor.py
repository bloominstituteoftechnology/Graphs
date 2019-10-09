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


def earliest_ancestor(ancestors, starting_node):

    queue = Queue()
    queue.enqueue([starting_node])
    visited_nodes = set()
    print(f"The queue size is {queue.size()}")
    has_parent = False
    longest_path = []
    while queue.size() > 0:
        current_path = queue.dequeue()
        print(f"current path: {current_path}")
        if len(current_path) > len(longest_path):
            longest_path = current_path
            print(f"Longest path: {longest_path}")
        elif len(current_path) == len(longest_path):
            if current_path[-1] < longest_path[-1]:
                longest_path = current_path
        vertex = current_path[-1]
        print(f"vertex: {vertex}")
        if vertex not in visited_nodes:
            visited_nodes.add(vertex)
            print(f"visited nodes: {visited_nodes}")
            for i in range(0, len(ancestors)):
                if ancestors[i][1] is vertex:
                    print(f"{ancestors[i][1]} has a parent!, it's {ancestors[i][0]}")
                    has_parent = True
                    test_path = list(current_path)
                    test_path.append(ancestors[i][0])
                    print(f"Test path: {test_path}")
                    queue.enqueue(test_path)
            if has_parent is False:
                print(f"{vertex} has no parents.  D:")
                print(f"Earliest ancestor: {-1}")
                return -1
    print(f"Earliest ancestor: {longest_path[-1]}")
    return longest_path[-1]
            
        # If vertex doesn't have parents:
            # return -1
        



        
# earliest_ancestor([
#         (1, 3), 
#         (2, 3), 
#         (3, 6), 
#         (5, 6), 
#         (5, 7), 
#         (4, 5), 
#         (4, 8), 
#         (8, 9), 
#         (11, 8), 
#         (10, 1)
#     ], 6)

earliest_ancestor([
    (1, 3), 
    (2, 3), 
    (3, 6), 
    (5, 6), 
    (5, 7), 
    (4, 5), 
    (4, 8), 
    (8, 9), 
    (11, 8), 
    (10, 1)
], 10)