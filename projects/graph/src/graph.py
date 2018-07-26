#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    """
    Represent a vertex with a label and possible connected component.
    """
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'v' + self.label

class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """
    def __init__(self):
        self.vertices = {}
        self.components = 0

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
        visited[root] = True
        print("Current Node:", root)
        print("Changes when visited: ", visited)
        # recur over all vertices adjacent to the current node
        for adjacents in self.vertices[root]:
            print("Check adjacent nodes: ", adjacents)
            if visited[adjacents] == False:
                self._dfs_helper(adjacents, visited)

    def DFS(self, vertex):
        """
        Depth-first Search (Recursive)
        """
        print("\n")
        print("Depth-First Search ")
        print("starting from vertex 3:")
        # mark all vertices as not visited
        visited = [False] * (len(self.vertices))
        print("Initially, all nodes are False: ", visited)
        # call recursive helper function to
        # print out DFS traversal
        self._dfs_helper(vertex, visited)


    def BFS(self, root):
        """
        Breadth-first Search (Boolean Method)
        """
        print("\n")
        print("Breadth-First Search ")
        print("starting from vertex 0:")
        # mark all vertices as not visited
        visited = [False] * (len(self.vertices))
        print("Initially, all nodes are False: ", visited)
        # init a queue as a list
        q = [] 
        # enqueue the root
        q.append(root)
        print("Queue with root value appended: ", q)
        # mark root node as visited
        visited[root] = True
        print("Root has been visited: ", visited)
        while q:
            # dequeue a vertex from the queue
            # and then print it
            print("Before Dequeued Root: ", root)
            print("Queue: ", q)
            root = q.pop(0)
            print("Dequeued Root: ", root)
            print("Queue after the Root's gone: ", q)
            print("Changes when visited: ", visited)
            # get all adjacent vertices of dequeued root
            # if adjacent vertexes have no been visted:
            # mark them as visted and enqueue them
            for adjacents in self.vertices[root]: 
                if visited[adjacents] == False:
                    q.append(adjacents)
                    visited[adjacents] = True

    def search(self, start, target=None, method='dfs'):
        """
        Search Graph with either DFS(stack) or BFS
        """
        print("\n")
        print("Search: ")
        quack = [start] # Queue or Stack, depending on method
        print("Initial Queue/Stack: ", quack)
        pop_index = 0 if method == 'bfs' else -1
        visited = set()
        print("Initial Visited: ", visited)

        while quack:
            current = quack.pop(pop_index)
            print("Current Position: ", current)
            if current == target:
                break
            visited.add(current)
            # add unvisited vertices to Queue/Stack(quack)
            print("Visited: ", visited)
            quack.extend(self.vertices[current] - visited)
            print("Quack: ", quack)
        
        return visited

    def find_components(self):
        """
        Identify components and update vertex component IDs.
        """
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                """
                Choose a Search Method:
                """
                # reachable = self.DFS(vertex)
                # reachable = self.BFS(vertex)
                reachable = self.search(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
