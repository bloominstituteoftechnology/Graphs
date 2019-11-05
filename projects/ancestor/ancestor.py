import sys
sys.path.append('../graph')
from graph import Graph
from util import Queue, Stack
def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for d in range(1,12):
        graph.add_vertex(d)
    for pair in ancestors:
        graph.add_edge(pair[0],pair[1])
   
    # # Create an empty queue and enqueue the starting vertex ID
    q = Queue()
    q.enqueue(starting_node)
    graph = Graph()
    # Create a Set to store visited vertices
    visited = set()
    # While the queue is not empty...
    while q.size() > 0:
        # Dequeue the first vertex
        v = q.dequeue
        # If that vertex has not been visited...
        if v not in visited:
            # Mark it as visited...
            visited.add(v)
            for neighbor in graph.vertices[v]:
                q.enqueue(neighbor)
            # Then add all of its neighbors to the back of the queue
