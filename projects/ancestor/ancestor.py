from util import Stack, Graph

# DFS
def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    # print("ancestors1", ancestors)
    stack = Stack()
    # Add starting_node to our stack
    stack.push([starting_node])  
    # Create an empty set to keep track of nodes visited
    visited = set()
    
    # While stack contains nodes
    while stack.size() > 0:
        # Pop first node
        path = stack.pop() # Path is first item in stack
        node = path[-1]  # Node is the last item in path
        print("node", node, "path", path)
        # If node has not yet been visited
        if node not in visited:
            if node == ancestors: 
                print("path2", path)
                return path  # Return path we've built so far
            # Add node to visited
            visited.add(node)
            print("visited", visited)
            # Get ancestors for each edge in item
            for next_node in Graph.get_neighbors(node):
                new_path = list(path)  # Make a copy of path
                new_path.append(next_node)  # Add new node to copy
                stack.push(new_path)  # Add new path to stack
    
