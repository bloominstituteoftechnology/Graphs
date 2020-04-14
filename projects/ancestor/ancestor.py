from projects.graph.util import Stack, Queue  # These may come in handy
from projects.ancestor.graph import Graph

def earliest_ancestor(ancestors, starting_node):
    parent = 0
    child = 1
    
    graph_child_to_parent = Graph()