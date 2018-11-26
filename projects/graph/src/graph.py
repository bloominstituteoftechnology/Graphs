"""
Simple graph implementation compatible with BokehGraph class.
"""

from draw import BokehGraph

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_edge(self, start, end, bidirectional=True):
        """Add an edge from start to end."""
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Error - vertices not in graph!")
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)
    """
    DFS(graph):
    for v of graph.verts:
        v.color = white
        v.parent = null

    for v of graph.verts:
        if v.color == white:
            DFS_visit(v)
    """

    def dft(self, starting_node, visited=None):
        """
        Depth first traversal using recursion
        """
        # Mark the node as visited
        if visited is None:
            # quese of visited nodes
            visited = []
        visited.append(starting_node)
        # For each child, if that child hasn't been visited, call dft() on that node
        for node in self.vertices[starting_node].edges:
            if node not in visited:
                self.dft(node, visited)
        return visited   

    """
    BFS(graph, startVert):
  for v of graph.vertexes:
    v.color = white

  startVert.color = gray
  queue.enqueue(startVert)

  while !queue.isEmpty():
    u = queue[0]  // Peek at head of queue, but do not dequeue!

    for v of u.neighbors:
      if v.color == white:
        v.color = gray
        queue.enqueue(v)

    """

    def bft(self, starting_node):
        visited = []
        # create an empty queue
        q = Queue()
        # Put starting vert in the queue
        q.enqueue(starting_node)
        while q.size() > 0:  # whlie queue is not empty...
            dequeued = q.dequeue() # Dequeue the first element
            visited.append(dequeued)  # Mark it as visited
            print(dequeued)
            for edge in self.vertices[dequeued].edges:  #For each child
                if edge not in visited:  # If it hasn't been visited
                    q.enqueue(edge)  # Add it to the back of the queue
        return visited


    def add_vertex(self, vertex, edges=()):
        if not set(edges).issubset(self.vertices):
            raise Exception("Error: Cannot have edge to nonexistent vertices")
        if vertex in self.vertices:
            raise Exception("Error: Vertex already exists.")
        self.vertices[vertex] = set(edges)


def main():
    graph = Graph()
    graph.add_vertex("0")
    graph.add_vertex("1")
    graph.add_vertex("2")
    graph.add_vertex("3")
    graph.add_vertex("4")
    graph.add_vertex("5")
    graph.add_vertex("6")
    graph.add_vertex("7")
    graph.add_edge("0", "1")
    graph.add_edge("0", "3")
    graph.add_edge("7", "5", False)

    b = BokehGraph(graph)
    b.show()


if __name__ == "__main__":
    main()
