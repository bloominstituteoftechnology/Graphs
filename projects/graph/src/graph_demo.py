#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph
import random

# exploration with random functions
random.seed(123)
print(random.random())
#help(random.shuffle)
x = [2,4,6,8,10]
random.shuffle(x)
print(x)

def main():
    pass  # TODO


if __name__ == '__main__':
    # TODO - parse argv
    main()
