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




test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
def earliest_ancestor(ancestors, starting_node):  
  # Make a an empty dictionary
  # Step number 1 reverse the order of the sets in the given list
  grand_parents = {}
  for ancestor in ancestors:
    if ancestor[1] not in grand_parents:      
      grand_parents[ancestor[1]] = set()   # grand_parents = { 3: ()}    
    grand_parents[ancestor[1]].add(ancestor[0])
  # checking the edge cases - return -1 not found.
  if starting_node not in grand_parents:
    return -1  
  # Make a stack
  stack = Stack()
  # Make a visited
  visited = []
  # Create a original list
  original = []
  # push first value in the stack
  stack.push([starting_node])
  # As long as stack is not empty run the while loop
  while stack.size() > 0:
    #  Create a path --
    path = stack.pop()
    # create a node as single number not as list ** remember this
    node = path[-1]
    # add node in the visited list
    if node not in visited:
      visited.append(node) 
      if len(path) > len(original):
        # replace the original with path
        original = path
      if len(path) == len(original) and path[-1] < original[-1]:
        original = path  
  
      if node in grand_parents:
        for parent in grand_parents[node]:
          new_path = path[:]     # new_path = [6]
          new_path.append(parent)  # new_path = [6,3]  # new_path = [6,3,5]
          stack.push(new_path) 

  return original[-1]      



     


       

  print(grand_parents)   

earliest_ancestor(test_ancestors,None)  

    