"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if not vertex in self.vertices:
            self.vertices[vertex] = set()
        else:
            print('This vertex is already part of the graph.')
            return

    def add_edge(self, vert1, vert2):
        # if both vert1 and vert2 are valid vertices found in self.vertices...
        if vert1 in self.vertices and vert2 in self.vertices:
            # if an edge has not already been created from vert1 to vert2, add edge to self.vertices
            if (not vert2 in self.vertices[vert1]) and (not vert1 in self.vertices[vert2]):
                self.vertices[vert1].add(vert2)
                self.vertices[vert2].add(vert1)
            # if the edge had already been created, print error message.
            else:
                print('This edge had already been created in the graph.')
                return
        # if one of vert1 and vert2 is an invalid vertex, print error message
        else:
            print('Please provide a valid set of vertices in the graph.')
            return
    
    def add_directed_edge(self, vert1, vert2):
        if vert1 in self.vertices and vert2 in self.vertices:
            if vert2 not in self.vertices[vert1]:
                self.vertices[vert1].add(vert2)
            else:
                print('This edge had already been created in the graph.')
                return
        # if one of vert1 and vert2 is an invalid vertex, print error message
        else:
            print('Please provide a valid set of vertices in the graph.')
            return
    # Breadth first traversal
    def bft(self, starting_vert):
        # create storage for vertices visited
        visited = []
        # create queue to maintain BFT order of vertices visited
        queue = [starting_vert]
        # While we have not finished checking all edges, as depicted by the number of elements left in the queue:
        while len(queue) > 0:
            # dequeue and check if element has been visited; if it hadn't, add it to the visited list, follow by adding its children vertices to the queue
            current_vert = queue.pop(0)
            if not current_vert in visited:
                visited.append(current_vert)
                for vert in self.vertices[current_vert]:
                    queue.append(vert)
        return visited
    
    # Depth first traversal
    def dft(self, starting_vert):
        # create storage for vertices visited
        visited = []
        # create stack to maintain BFT order of vertices visited
        stack = [starting_vert]
        # While we have not finished checking all edges, as depicted by the number of elements left in the queue:
        while len(stack) > 0:
             # dequeue and check if element has been visited; if it hadn't, add it to the visited list, follow by adding its children vertices to the stack
            current_vert = stack.pop(-1)
            if current_vert not in visited:
                visited.append(current_vert)
                for vert in self.vertices[current_vert]:
                    stack.append(vert)
        return visited

    # Depth first traversal - recursive
    def dft_recursive(self, starting_vert):
        visited = []
        def helper_method(hm_vert):
            if hm_vert != None and hm_vert not in visited:
                visited.append(hm_vert)
                for child_vert in self.vertices[hm_vert]:                  
                    recursive_var = helper_method(child_vert)
                    if recursive_var != None:
                        visited.append(recursive_var)
        helper_method(starting_vert)
        return visited

    def bfs(self, starting_vert, target_vert):
        visited = []
        queue = [[starting_vert]]
        while len(queue) > 0:
            current_path = queue.pop(0)
            current_vert = current_path[-1]
            # print(current_path)
            if current_vert == target_vert:
                return current_path
            if current_vert not in visited:
                visited.append(current_vert)
                for child_vert in self.vertices[current_vert]:
                    # print(current_path, child_vert)
                    new_path = list(current_path)
                    new_path.append(child_vert)
                    # print(temp_var)
                    queue.append(new_path)
        return None
    
    def dfs(self, starting_vert, target_vert):
        visited = []
        stack = [[starting_vert]]
        while len(stack) > 0:
            current_path = stack.pop(-1)
            current_vert = current_path[-1]
            # print(current_path)
            if current_vert == target_vert:
                return current_path
            if current_vert not in visited:
                visited.append(current_vert)
                for child_vert in self.vertices[current_vert]:
                    # print(current_path, child_vert)
                    new_path = list(current_path)
                    new_path.append(child_vert)
                    # print(temp_var)
                    stack.append(new_path)
        return None
    
    def dfs_recursive(self, starting_node, target_vert, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path =[]
        visited.add(starting_node)
        extended_path = list(path)
        extended_path.append(starting_node)
        if starting_node == destination_node:
            return extended_path
        for child in self.vertices.edges:
            if child not in visited:
                new_path = self.dfs_recursive(child,destination_node, visited, extended_path)
                if new_path:
                    return new_path
        return None
   

# test
graph = Graph()  # Instantiate your graph
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_directed_edge('1', '2')
graph.add_directed_edge('2', '3')
graph.add_directed_edge('2', '4')
graph.add_directed_edge('4', '6')
graph.add_directed_edge('4', '7')
graph.add_directed_edge('6', '3')
graph.add_directed_edge('7', '6')
graph.add_directed_edge('7', '1')
graph.add_edge('3', '5')

# print(graph.vertices)
# print(graph.bft('1'))
# print(graph.dft('1'))
print(graph.dfs('1','5'))