class Node:

    def __init__(self, index):
        self.index = index
        self.children = []
        self.parents = []

    def __repr__(self):
        index = self.index
        parents = [parent.index for parent in self.parents]
        children = [child.index for child in self.children]
        return f'Node: {index} Parents: {parents} Children: {children}'

    def addChild(self, child):
        self.children += [child]

    def addParent(self, parent):
        self.parents += [parent]


def ancestorSearch(node, depth=0):
    if len(node.parents) == 0:
        if depth == 0:
            return -1
        else:
            return [node, depth]

    if len(node.parents) == 1:
        return ancestorSearch(node.parents[0], depth + 1)

    if len(node.parents) == 2:
        left = ancestorSearch(node.parents[0], depth + 1)
        right = ancestorSearch(node.parents[1], depth + 1)
        if left[1] > right[1]:
            return left
        elif left[1] < right[1]:
            return right
        else:
            if left[0].index < right[0].index:
                return left
            else:
                return right


def earliest_ancestor(ancestors, starting_node):
    nodes = {}

    for node in ancestors:
        index = node[0]
        child = node[1]

        if index not in nodes:
            nodes[index] = Node(index)

        if child not in nodes:
            nodes[child] = Node(child)

        nodes[index].addChild(nodes[child])
        nodes[child].addParent(nodes[index])

    result = ancestorSearch(nodes[starting_node])

    if result == -1:
        return result
    else:
        return result[0].index
