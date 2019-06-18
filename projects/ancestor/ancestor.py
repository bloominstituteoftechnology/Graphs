import sys
from collections import defaultdict()

individual = int(input())
family = defaultdict(list)
for line in sys.stdin.readline():
    parent, child = line.split()
    family[parent].append[child]


def earliest_ancestor(individual, dataset):
    pass