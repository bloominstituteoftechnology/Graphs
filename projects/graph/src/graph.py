"""
Simple graph implementation compatible with BokehGraph class.
"""


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

    def bfs(self, starting_vert, target_vert):
        visited = []
        queue = [starting_vert]
        while len(queue) > 0:
            current_vert = queue.pop(0)
            # print(current_vert)
            if current_vert == target_vert:
                visited.append(current_vert)
                return visited
            else:
                if not current_vert in visited:
                    visited.append(current_vert)
                    for vert in self.vertices[current_vert]:
                        queue.append(vert)
        return 'No path found that linked vertex ' + starting_vert + ' to vertex ' + target_vert
    
    def dfs(self, starting_vert, target_vert):
        visited = []
        stack = [starting_vert]
        while len(stack) > 0:
            current_vert = stack.pop(len(stack)-1)
            # print(current_vert)
            if current_vert == target_vert:
                visited.append(current_vert)
                return visited
            else:
                if not current_vert in visited:
                    visited.append(current_vert)
                    for vert in self.vertices[current_vert]:
                        stack.append(vert)
        return 'No path found that linked ' + starting_vert + ' to ' + target_vert
# test
graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('0', '4')
graph.add_edge('3','0')
print(graph.vertices)
print(graph.bfs('3', '1'))
print(graph.dfs('0', '3'))