import math
"""
===== DFS =====
1. Starting Node + Target Node
2. Add [starting_node] to path, and push it to stack
3. pop last item from stack
4. check the last item in the path, for instance [1, 2, 4, 6, 7]... check 7 (path[-1])
5. add path[-1] to your visited
6. get neighbors of path[-1]
7. add to your path, so for each neighbor, create a path copy, add the neighbor to end of path
8. push your new path to your stack
9. for instance, if neighbors of 7 are 10, 12, 13, 6, but 6 has been visited
10. [1, 2, 4, 6, 7, 10], [1, 2, 4, 6, 7, 12], [1, 2, 4, 6, 7, 13] will be added to stack
11. when path[-1] is your target, stop and return the path
"""
"""
==== BFS ====
1. Do everything above with a queue instead of a stack
"""


# testing = [123]

# cloned = [*testing]

# cloned +=[345]

# print(cloned)




