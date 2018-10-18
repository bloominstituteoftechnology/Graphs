"""
Simple graph implementation compatible with BokehGraph class.
"""

from random import randint

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, vertices_list={}):
        self.vertices_list = vertices_list

    def show_graph(self):
        print(self.vertices_list)

    def add_vertex(self, vertex):
        self.vertices_list[vertex] = set()

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.vertices_list:
            raise Exception(f"⚠️ Vertice {from_vertex} is not in the graph")
        if to_vertex not in self.vertices_list:
            raise Exception(f"⚠️ Vertice {to_vertex} is not in the graph")
        # if edge already in set
        if to_vertex in self.vertices_list[from_vertex]:
            return False
    
        self.vertices_list[from_vertex].add(to_vertex)
        return True

    def randomise_graph(self, num_vertices, num_edges):
        # v * v edges to fill all vertices 
        # including vertex pointing itself
        if num_edges > num_vertices * num_vertices:
            print(f"⚠️ Number of edges exceeds maximum")

        for vertex in range(0, num_vertices):
            self.add_vertex(str(vertex))

        edge = 0

        # while loop to create new edge
        while edge < num_edges:
            from_vertex = str(randint(0, num_vertices - 1))
            to_vertex = str(randint(0, num_vertices - 1))
            if self.add_edge(from_vertex, to_vertex):
                edge += 1

        print(self.vertices_list) 

    def breadth_first_search(self, start, target):
        """
        Search each vertex in vertices_list in FIFO
        to check whether target is connected within graph
        """
        queue = [start]
        visited = set([start])
        # print(self.vertices_list)

        while len(queue) > 0:
            removed_vertex = queue.pop(0)
            visited.add(removed_vertex)  
            # print(queue)      

            if removed_vertex == target:
                print(f"{target} is found")
                return target
            else:
                for connected_vertex in self.vertices_list[removed_vertex]:
                    if connected_vertex not in visited:
                        queue.append(connected_vertex)

        print(f"{target} is not in the graph or not connected by {start}")
        return False
    
    def depth_first_search(self, start, target, visited = set()):
        """
        Search each vertex in vertices_list in LIFO
        to check whether target is connected within graph
        """
        if len(visited) == 0:
            visited = set([start])

        for connected_vertex in self.vertices_list[start]:
            # if visited
            if connected_vertex in visited:
                return
            # if a match
            if connected_vertex == target:
                print(f"{target} is found")
                return target
            else:
                visited.add(connected_vertex)
                self.depth_first_search(connected_vertex, target, visited)
         
graph = Graph()  # Instantiate graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_vertex('4')
# graph.add_edge('0', '1')
# graph.add_edge('0', '2')
# graph.add_edge('2', '3')
# graph.add_edge('3', '4')
# graph.randomise_graph(10, 100)
# graph.breadth_first_search('0', '2')
# graph.depth_first_search('0', '4')