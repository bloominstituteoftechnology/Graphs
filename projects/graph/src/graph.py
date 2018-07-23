#!/usr/bin/python
#Start Here

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        graph = {
            '0': set()
             '1': ['2'],
             '2': ['1', '7'],
             '3': ['8'],
             '4': set(),
             '5': ['6', '10'],
             '6': ['5', '7'],
             '7': ['2','6', '8'],
             '8': ['3', '7', '9', '13'],
             '9': ['8', '14'],
             '10': ['5'],
             '11': set(),
             '12': ['13'],
             '13': ['8', '12', '14'],
             '14': ['9', '13'],
             '15': ['16'],
             '16': ['15', '17'],
             '17': ['16'],
             '18': set(),
             '19': set(),
             }
