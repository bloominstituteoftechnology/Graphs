class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            KeyError('Error')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()

        queue.enqueue(starting_vertex)
        visited_path = set()

        while queue.size() > 0:
            dequeued = queue.dequeue()
            if dequeued not in visited_path:
                visited_path.add(dequeued)
                # print(dequeued)
                for items in self.vertices[dequeued]:
                    queue.enqueue(items)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()

        s.push(starting_vertex)
        visited_path = set()

        while s.size() > 0:
            depoped = s.pop()
            if depoped not in visited_path:
                # print(depoped)
                visited_path.add(depoped)

                for items in self.vertices[depoped]:
                    s.push(items)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        print(starting_vertex)
        visited.add(starting_vertex)
        for vertice in self.vertices[starting_vertex]:
            if vertice not in visited:
                self.dft_recursive(vertice, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()

        visited = set()
        queue.enqueue([starting_vertex])
        while queue.size() > 0:
            path = queue.dequeue()
            vert = path[-1]
            if vert not in visited:
                if vert == destination_vertex:
                    return path

                visited.add(vert)
            for next_vert in self.vertices[vert]:
                new_path = list(path)
                new_path.append(next_vert)
                queue.enqueue(new_path)

        return None

    def dfs(self, starting_vertex, destination_vertex, visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()

        visited = set()
        stack.push([starting_vertex])
        while stack.size() > 0:
            path = stack.pop()
            vert = path[-1]
            if vert not in visited:
                if vert == destination_vertex:
                    return path

                visited.add(vert)
            for next_vert in self.vertices[vert]:
                new_path = list(path)
                new_path.append(next_vert)
                stack.push(new_path)

        return None


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(8)
    graph.add_vertex(9)
    graph.add_vertex(10)
    graph.add_vertex(11)
    for a in ancestors:
        graph.add_edge(a[1], a[0])
    stack = Stack()

    stack.push(starting_node)
    visited = []

    while stack.size() > 0:
        removed = stack.pop()
        for items in sorted(graph.vertices[removed]):
            stack.push(items)

        if removed not in visited and removed != starting_node:
            visited.append(removed)

    if len(visited) < 1:
        return -1
    elif len(visited) == 1:
        for v in visited:
            return v
    return visited[len(visited) - 1]

