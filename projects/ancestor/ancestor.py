from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node):
    queue = Queue()

    for item in ancestors:
        