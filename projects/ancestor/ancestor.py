class Stack:
	def __init__(self):
		self.stack = []
	def push(self, value):
		self.stack.append(value)
  
	def size(self):
		return len(self.stack)

	def pop(self):
		if self.size() > 0:
			return self.stack.pop(-1)
		else:
			return 0
    

        
        
    


def earliest_ancestor(ancestors, starting_node):
    pass