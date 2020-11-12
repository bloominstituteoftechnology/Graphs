


# Singly Linked List
from typing import no_type_check_decorator


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

        # self.prev if DLL

# LL traversal
current = node
while current is not None:
    current = current.next


class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BST Traversal
## BFT or DFT
### Stack, Queue

while node is not None:
    recurse(self.left)
    recurse(self.right)


class GraphNode:
    def __init__(self, value):
        self.value = 'B'

        # options: dictionary, array, set
        # B's connections
        self.connections = set('A', 'C', 'D')
        
        # A's connections
        self.connections = set('B')

        # D's connections - it's a zero - Billy no mates!
        self.connections = set()


# outbound vs inbound conections?

# Grpah terminology for 2-way vs 1-way connections
## undirected graph vs directed graph
## (FB, LinkedIn) vs (instagram, Twitter, TikTok)

## Graph Traversals

## DFT, stack
### check every node once, check every connection once

# make a stack
stack = Stack('A', 'B')
# make a set to track visited
visited = set('A', 'B', 'D', 'C')

# put the start node into the stack

# while the stack isn't empty

## pop off the top of the stack, this is the current node
current_node = 'B'
## check if we have visited this node
### if not, add it to our visited set
### and add each of it's neighbors to our stack
#### started with just A as current node and moved on ^^^^

## Time complexity? O(n)
## how many times do we visit each node? once
### how many times did we check each connection? once

## O(number of nodes + number of connections)
### O(n + m)
## so linear! 

# BFT, Queue
# ---->>>>
q = Queue('D', 'C')

# make a set to track visited
visited = set('A', 'B')
# enqueue the start node
# while our queue isn't empty
## dequeue from front of line, this is our current node
current_node = 'B' # then move to 'C', add to visited, get neighbors, add to queue
## check if we've visited the node yet
### if not, add to visited
### get it's neighbors, for each add to queue
neighbors = set('C', 'D')
## RIPPLES! A) B) CD) EFG) ')' is the ripple

# Time complexity? O(n)
## visit every node once, visit every edge once
## O(n + m)
## O(node + edge)
## linear as well!

# DFT vs. BFT
## same time complexity, each just as fast
## DFT can be done recursively
## BFT can find shorter path
