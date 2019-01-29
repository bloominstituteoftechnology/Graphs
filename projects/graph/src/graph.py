"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {
        }

    def add_vertex(self, string):
        # adds vertexs and defaults it to a set
        self.vertices[string] = set()

    def add_edge(self, from_vertex, to_vertex):
        # check to see if theres a key with the name sent to from_vertex
        try:
            self.vertices[to_vertex].add(from_vertex)
            self.vertices[from_vertex].add(to_vertex)
        except:
            print('there is no vertex named', to_vertex, ' in the graph')

    def bst_traversal(self, start_node):
        nodes = []
        visited = []
        node = start_node
        nodes.append(node)

        # enqueue the starting node
        while nodes:
            node = nodes.pop(0)
            # check if node has edges
            if len(self.vertices[node]) is 0:
                # dequeue next num
                visited.append(node)
                pass
            else:
                # dequeue first node
                edge_nodes = list(self.vertices[node].copy())
                visited.append(node)
                for i in edge_nodes:
                    if i in visited or i in nodes:
                        pass
                    else:
                        nodes.append(i)
                print("this is nodes", nodes)

        print("BFT has returned ", visited)

    def dft_traversal(self, start_node):
        nodes = []
        visited = []
        node = start_node
        nodes.append(node)

        # enqueue the starting node
        while nodes:

            node = nodes.pop()
            # check if node has edges
            if len(self.vertices[node]) is 0:
                # dequeue next num
                visited.append(node)

                pass
            else:
                # dequeue first node
                edge_nodes = list(self.vertices[node].copy())
                visited.append(node)
                for i in edge_nodes:
                    if i in visited or i in nodes:
                        pass
                    else:
                        nodes.append(i)

                print("this is nodes", nodes)
        print("DFT has returned", visited)
        pass

    def bfs_search(self, starting_node, target_node):
        nodes = []
        visited = []
        nodes.append(list(starting_node))

        # enqueue the starting node
        while nodes:
            print("this is nodes before popping:", nodes)
            list_of_nodes = nodes.pop(0)
            copied_list = list_of_nodes.copy()
            print("this is your copied list: ", copied_list)
            print("this is the indexed list we are grabbing: ", list_of_nodes)
            node = list_of_nodes.pop()
            print("this is your node: ", node)
            # check if node has edges

            if len(self.vertices[node]) is 0:
                # dequeue next num
                visited.append(node)
                pass
            else:
                # dequeue first node
                if node == target_node:
                    print("shortest path is: ", copied_list)
                    return True
                else:
                    edge_nodes = list(self.vertices[node].copy())
                    visited.append(node)
                    for i in edge_nodes:
                        if i in visited or i in nodes:
                            pass
                        else:
                            print("this is a path to: ", i)
                            copy_list = copied_list.copy()
                            copy_list.append(i)
                            print(copy_list)
                            nodes.append(copy_list)
        return False

    def dfs_search(self, starting_node, target_node):
        nodes = []
        visited = []
        node = starting_node
        nodes.append(node)

        # enqueue the starting node
        while nodes:

            node = nodes.pop()
            # check if node has edges
            if len(self.vertices[node]) is 0:
                # dequeue next num
                visited.append(node)

                pass
            else:
                # dequeue first node
                if node == target_node:
                    return True
                else:
                    edge_nodes = list(self.vertices[node].copy())
                    visited.append(node)
                    for i in edge_nodes:
                        if i in visited or i in nodes:
                            pass
                        else:
                            nodes.append(i)
        return False


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('3', '5')
graph.add_edge('1', '4')
print(graph.bfs_search('0', "4"))
# print(graph.dfs_search('0', "4"))
# graph.add_edge('0', '4')
