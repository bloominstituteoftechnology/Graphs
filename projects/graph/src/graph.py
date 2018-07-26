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

    def _dfs_helper(self, root, visited):
        """
        Recursive helper function for Depth-First Search
        """
        # mark current node visited
        visited[int(root)] = True
        print("Current Node:", root)
        print("Visited Status Change: ", visited)
        # recur over all vertices adjacent to the current node
        for adjacents in self.vertices[root]:
            if visited[int(adjacents)] == False:
                self._dfs_helper(adjacents, visited)

    def DFS(self, vertex):
        """
        Depth-first Search (Recursive)
        """
        # mark all vertices as not visited
        visited = [False] * (len(self.vertices))
        print("Initially, all nodes are False ", visited)
        # call recursive helper function to
        # print out DFS traversal
        self._dfs_helper(vertex, visited)

    def BFS(self, root):
        """
        Breadth-first Search (Boolean Method)
        """
        # mark all vertices as not visited
        visited = [False] * (len(self.vertices))
        print("Initially, all nodes are False ", visited)
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

        # def connected_component(self, component):
        #     connected_components = []
        #     visited = set()

        #     for v in graph.vertices:
        #         if v not in visited:
        #             visited.update(component)
        #             connected_components.append(component)

def main():
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

    print("\n")
    print("The Graph: ", graph.vertices)
    print("\n")
    print("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
    graph.BFS('2')
    print("\n")
    print("Following is Depth First Traversal"
                  " (starting from vertex 2)")
    graph.DFS('2')
    print("\n")

if __name__ == '__main__':
    main()
