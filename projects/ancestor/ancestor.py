from util import Queue
def earliest_ancestor(ancestors, starting_node):
    
    queue = Queue()
    queue.enqueue([starting_node])
    visited_nodes = set()
    has_parent = False
    longest_path = []

    while queue.size() > 0:
        current_path = queue.dequeue()
        
        if len(current_path) > len(longest_path):
            longest_path = current_path

        elif len(current_path) == len(longest_path):

            if current_path[-1] < longest_path[-1]:
                longest_path = current_path

        vertex = current_path[-1]

        if vertex not in visited_nodes:
            visited_nodes.add(vertex)

            for i in range(0, len(ancestors)):
                print(ancestors[i][1])
                
                if ancestors[i][1] is vertex:
                    has_parent = True
                    test_path = list(current_path)
                    test_path.append(ancestors[i][0])
                    queue.enqueue(test_path)
            if has_parent is False:
                return -1
   
    return longest_path[-1] 
