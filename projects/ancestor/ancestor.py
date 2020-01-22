from util import Stack, Graph

ancestors_data = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# DFS
def earliest_ancestor(ancestors, starting_node):
    ancestor_tree = Graph()
    # Iterate through ancestors_data
    for ancestor in ancestors:  
        # Iterate through each item in every set
        for vert in ancestor:
            # Add vertices to ancestor_tree
            ancestor_tree.add_vertex(vert)
    print("ancestor tree", ancestor_tree.vertices)
    
    for ancestor in ancestors:
        # Add edges
        ancestor_tree.add_edge(ancestor[1], ancestor[0])
    # print("neighbors", ancestor_tree.get_neighbors(5))

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
                return node  # Return node 
            # Add node to visited
            visited.add(node)
            print("visited", visited)
            # Get ancestors for each edge in item
            for next_node in ancestor_tree.get_neighbors(node):
                new_path = list(path)  # Make a copy of path
                new_path.append(next_node)  # Add new node to copy
                stack.push(new_path)  # Add new path to stack


print('earliest ancestor', earliest_ancestor(ancestors_data, 8))