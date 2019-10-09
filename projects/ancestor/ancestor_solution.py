#!/usr/bin/env python
from typing import List, Tuple
from collections import defaultdict

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

    @property
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = defaultdict(set)

    #def add_vertex(self, v: int):
    #   pass # not needed cuz defaultdict

    def add_edge(self, tail: int, head: int):
        self.vertices[tail].add(head)
        self.vertices[head]
        pass

def earliest_ancestor(ancestors: List[Tuple[int, int]],
                      starting_vertex: int) -> int:
    # build
    graph: Graph = Graph()

    for tail, head in ancestors:
        # build edges in reverse
        graph.add_edge(head, tail)

    qq: Queue = Queue()
    qq.enqueue([starting_node])

    max_path_length: int = 1
    earliest_ancestor: int = -1

    while qq.size > 0:
        path = qq.dequeue()
        v: int = path[-1]

        if (len(path)>=max_path_length and
            v<earliest_ancestor) or \
           len(path) > max_path_length):
            earliest_ancestor = v
            max_path_length = len(path)

        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            qq.enqueue(path_copy)

    return earliest_ancestor
