# Earliest Ancestor

# so were goign to be given a dataset and an id
# of an individual of that dataset as arguments.

# an individual is represented as an id.

# individual ID's are unique.

# we could represent a data set as a tree like so:
'''
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
'''
# with the sample input looking something like:
'''
Example input
  6

  1 3
  2 3
  3 6
  5 6
  5 7
  4 5
  4 8
  8 9
  11 8
  10 1
Example output
  10
'''


'''
Clarifications:

The input will not be empty.
There are no cycles in the input.
There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
IDs will always be positive integers.
A parent may have any number of children.
'''

# off the bat it seems to me like were really only concerned with parent relationships.
# were never going down the graph, only searching up.

# we can create a graph which specifies parents to nodes such as:
'''
{
    node: [parent]
    node: [parent, parent]
    node: []
}
'''

# then, starting at our selected node, check that we have any parents

# if no parents are found, we can simply return -1
# if there are multiple closest common ancestors, i.e. in the above example:
# 8 is a child of both 4 and 11
# we return the parent with the lowest numeric ID


# heres my plan

# 1. populate a graph in the fashion shown above..
# 2. check to see if the list at that graph node is empty. if it is, return -1
# 3. if its not, wel create a stack, initialize with our first ancestor,
# and loop over each of the first common ancestors.
# 4. wel create a list for each ancestor addition, starting with our starting node, and append the ancestor
# 5. now we have a Stack (havent decided yet) of all possible relationships 1 ancestor away.
# 6. wel continue to do this until were at the top of each ancestors list
# 7. we can now check to see which list is the longest/handel all cases

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def search_ancestors(target, parent_rel_tree, lineages, cur_list):
    new_cur_list = cur_list.copy()
    new_cur_list.append(target)

    if target not in parent_rel_tree:
        lineages.push(new_cur_list)
        return
    else:
        for parent in parent_rel_tree[target]:
            search_ancestors(parent, parent_rel_tree, lineages, new_cur_list)


def closest_ancestor(target, relationships):
    parent_rel_tree = {}
    for relationship in relationships:
        if relationship[1] in parent_rel_tree:
            parent_rel_tree[relationship[1]].append(relationship[0])
        else:
            parent_rel_tree[relationship[1]] = [relationship[0]]

    linages = Stack()
    linages.push([target])

    search_ancestors(target, parent_rel_tree, linages, [])
    print(linages.stack)


# test relationships
rels = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7],
        [4, 5], [4, 8], [8, 9], [11, 8], [10, 1]]

closest_ancestor(9, rels)
