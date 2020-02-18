class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


def earliest_ancestor(ancestors, starting_node):
    # Answer will hold the earliest ancestor answer[0] and the amount of edges to reach it answer[1]
    answer = [None, None]

    # Adjacency list for all nodes/edges in ancestors
    ancestor_dictionary = {}

    # Add all nodes and edges to adjacency list
    for a in ancestors:
        if a[0] in ancestor_dictionary:
            ancestor_dictionary[a[0]].add(a[1])
        else:
            ancestor_dictionary[a[0]] = set()
            ancestor_dictionary[a[0]].add(a[1])

    # Set up a reverse depth first search of the nodes.
    stack = Stack()
    visited = set()
    stack.push(starting_node)
    while stack.size() > 0:
        child = stack.pop()


        # If we are currently not on the first node, do a top down DFS of the nodes to find the length of any connecting path to the original child
        if child != starting_node:

            while True:
                stack_2 = Stack()
                visited_2 = set()
                stack_2.push([child])
                while stack_2.size() > 0:
                    current_path = stack_2.pop()
                    current_node = current_path[-1]
                    
                    #Here we have reached the base node
                    if current_node == starting_node:
                        # If nothing has been put in answer, we use the current value of 'child' as our earliest ancestor.
                        # We also set the length of the path to indicate how many edges there are to get there.
                        if answer[0] is None:
                            answer[0] = child
                            answer[1] = len(current_path)
                        
                        # If an answer already exists, we check to see if the current path is longer than the existing answer.
                        # If the current path is longer, we overwrite the ancestor and edge length
                        elif answer[1] < len(current_path):
                            answer[0] = child
                            answer[1] = len(current_path)
                        # if the edge length of the existing answer (answer[1]) equals the current path length, we overwrite it if the current ancestor integer saved in 'child' is lower than the one currently saved in answer[0].
                        elif answer[1] == len(current_path) and answer[0] > child:
                            answer[0] = child
                            answer[1] = len(current_path)
                    
                    # Add the node we are looking at to our visited set if we haven't worked with it yet
                    if current_node not in visited_2:
                        visited_2.add(current_node)

                        # If the current node has connections, we toss those on the stack and continue the loop
                        if current_node in ancestor_dictionary:
                            edges = ancestor_dictionary[current_node]
                            for edge in edges:
                                stack_2.push(current_path + [edge])
                                
                # Once we've checked everything in the stack, break the loop and continue with the outer reverse DFS functionality
                break

        # Check if there are parents to the current child node
        # If there are parents that have not been visited, add the to the stack
        for item in ancestor_dictionary:
            if child in ancestor_dictionary[item] and item not in visited:
                visited.add(item)
                stack.push(item)

    # Return earliest answers. If there are no parents, return -1
    if answer[0] is not None:
        return answer[0]
    else:
        return -1