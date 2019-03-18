"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {
                    0: {1, 67},
                    1: {0, 12, 19, 21, 7},
                    12: {1, 19},
                    19: {1, 12, 21},
                    21: {7, 1, 19, 31, 14},
                    7: {1, 21},
                    14: {21},
                    31: {21},
                    67: {0}
                }
        # self.vertices = {}
        # self.vertices = { 
        #                 0: {1, 2}, 
        #                 1: {0, 3, 4}, 
        #                 2: {0, 5, 6}, 
        #                 3: {1, 7, 8}, 
        #                 4: {1, 9, 10}, 
        #                 5: {2, 11, 12}, 
        #                 6: {2, 13, 14}, 
        #                 7: {3}, 
        #                 8:{3}, 
        #                 9: {4}, 
        #                 10: {4}, 
        #                 11: {5}, 
        #                 12: {5}, 
        #                 13: {6}, 
        #                 14: {6}  
        #                 }

    
    def add_vertex(self, value):
        if value in self.vertices:
            return ' The vertex already exists'

        self.vertices[value] = set()

    def add_edge(self, v1, v2):
        if v1 not in self.vertices or v2 not in self.vertices:
            return 'One of these vertices does not exist'
        self.vertices[v1].add(v2)
        self.vertices[v2].add(v1)

    def bf_traverse(self, start):
        q = [start]
        visited = []
        while len(q) > 0:
            # print('visited', visited)
            # print('q', q)
            cur_node = q.pop(0)
            if cur_node not in visited:
                visited.append(cur_node)
                # print(visited)
                for node in self.vertices[cur_node]:
                    q.append(node)
        return visited
    
    def bf_search(self, start, target):
        q = [[start]]
        visited = {}
        while len(q) > 0:
            path = q.pop(0)
            new_node = path[-1]
            if new_node == target:
                return path
            else:
                if new_node not in visited:
                    visited[new_node] = path
                    for item in self.vertices[new_node]:
                        new_path = list(path)
                        new_path.append(item)
                        q.append(new_path)
        return False


    def df_traverse(self, start):
        # create a stack
        s = [start]
        # visited list
        visited = []
        # go through the loop
        while len(s) > 0:
            # pop the last item in the stack
            cur_node = s.pop(0)
            # check if its in visited
            if cur_node not in visited:
                # if not add it to the visited
                visited.append(cur_node)
                # add it's children to stack
                for item in self.vertices[cur_node]:
                    s.insert(0, item)
        return visited

    def dft_recursive(self, start, visited=[]):
        if start not in visited:
            visited.append(start)
            for item in self.vertices[start]:
                self.dft_recursive(item, visited)
        return visited



    #     pass
        # q = [start]
        # What is the base case of recursive traverse?
        # in recursive: We get the start. Teh visited list passed in 



# x = {1, 2, 3, 4, 5}
# for i in range(len(x), 0, -1):
#     print('from set', x[i])

graph = Graph()  # Instantiate your graph
# print('bf traversal', graph.bf_traverse(0))
print('bf search for 14', graph.bf_search(0, 14))
print('bf search for 67', graph.bf_search(0, 67))
print('bf search for 99', graph.bf_search(0, 99))
# print('df traversal', graph.df_traverse(0)) # yyp
# print('dft recursive', graph.dft_recursive(0))

# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_vertex('4')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# graph.add_edge('0', '4')
# print("Vertices:",graph.vertices)
