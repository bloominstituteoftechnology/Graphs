from typing import List, Dict, Optional, Tuple, Set
from collections import defaultdict


def earliest_ancestor(ancestors: List[Tuple[int, int]],
                      starting_node: int) -> int:
    """ solve earliest ancestor """

    def get_adjacency_set_from_edge_tuples(
            edges: List[Tuple[int, int]]) -> Dict[int, Set[int]]:
        """ take a list of edges and return an adjacency set"""
        vertices = defaultdict(set)
        for tail, head in edges:
            vertices[head].add(tail)
        return vertices

    def bfs_distances(ancestors: Dict[int, Set[int]],
                      starting_node: int) -> Dict[int, int]:
        """ do bfs and return dictionary of all the distances
            reference: https://youtu.be/s-CYnVz-uh4 37 minutes
        """
        level: Dict[int, int] = {starting_node: 0}
        parent: Dict[int, Optional[int]] = {starting_node: None}
        i: int = 1
        frontier: List[int] = [starting_node]
        while frontier:
            next = []
            for u in frontier:
                for v in ancestors[u]:
                    if v not in level.keys():
                        level[v] = i
                        parent[v] = u
                        next.append(v)
            frontier = next
            i += 1

        return level

    levels = bfs_distances(get_adjacency_set_from_edge_tuples(ancestors),
                           starting_node)
    curr_earliest = None
    curr_max = -99

    for node, level in levels.items():
        if level==curr_max:
            # If there is more than one ancestor tied for "earliest",
            # return the one with the lowest numeric ID.
            curr_earliest = min(node, curr_earliest)
        elif level > curr_max:
            # the main "get max" logic
            curr_max = level
            curr_earliest = node

    if curr_earliest==starting_node:
        return -1 # -1 is the identifier for when yourself is your earliest ancestor.
    else:
        return curr_earliest
