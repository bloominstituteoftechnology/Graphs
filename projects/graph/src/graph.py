#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """
    def __init__(self):
        self.vertices = {}

    # def add_vertex_original(self, vertex):
    #     self.vertices[vertex] = set()

    # def add_edge_original(self, node_a, node_b):
    #     self.vertices[node_a].add(node_b)

    def add_vertex(self, vertex, edges=()):
        """
        Adds a new vertex, optionally with edges to other vertices.
        """
        if vertex in self.vertices:
            raise Exception('Error: this vertex already exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot have edge to nonexistent vertices')
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        """
        Add an edge(default: bidirectional) between two vertices.
        """
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Vertices to connect not in graph')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def DFS(self):
        """
        Depth-first Search (Stack?)
        """
        pass
    
    
    def BFS(self, root):
        """
        Breadth-first Search (Boolean Method)
        """
        # mark all vertices as not visited
        visited = [False] * (len(self.vertices))
        print("initially, all nodes are False ", visited)
        # init a queue as a list
        q = [] 
        # enqueue the root
        q.append(root)
        print("Queue with root value appended: ", q)
        # mark root node as visited
        visited[int(root)] = True
        print("Root has been visited: ", visited)
        while q:
            # dequeue a vertex from the queue
            # and then print it
            root = q.pop(0)
            print("Dequeued Root: ", root)
            print("Queue after the Root's gone: ", q)
            print("Root still visited -> ", visited)
            # get all adjacent vertices of dequeued root
            # if adjacent vertexes have no been visted:
            # mark them as visted and enqueue them
            for adjacents in self.vertices[root]: 
                if visited[int(adjacents)] == False:
                    q.append(adjacents)
                    visited[int(adjacents)] = True

# def main():
graph = Graph()

graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')

graph.add_edge('0', '1')
graph.add_edge('0', '2')
graph.add_edge('1', '2')
graph.add_edge('2', '0')
graph.add_edge('2', '3')
graph.add_edge('2', '3')

# graph.add_vertex(0)
# graph.add_vertex(1)
# graph.add_vertex(2)
# graph.add_vertex(3)

# graph.add_edge(0, 1)
# graph.add_edge(0, 2)
# graph.add_edge(1, 2)
# graph.add_edge(2, 0)
# graph.add_edge(2, 3)
# graph.add_edge(2, 3)

# print(graph.vertices)
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")

# graph.BFS(graph.vertices)
graph.BFS('2')

# if __name__ == '__main__':
#     main()


# connected_components = []
# visited = set()

# for v in graph.vertices:
#     if v not in visited:
#         visited.update(component)
#         connected_components.append(component)