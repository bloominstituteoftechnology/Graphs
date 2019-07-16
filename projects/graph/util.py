class Queue():
  def __init__(self):
    self.queue = []
  
  def enqueue(self, value):
    self.queue.append(value)
  
  def dequeue(self):
    if self.size() > 0:
      return self.queue.pop(0)['value']
    else:
      return None
  
  def size(self):
    return len(self.queue)
  
  def get(self, index = None):
    if index is None:
      return self.queue
    else:
      return self.queue[index]

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
  
  def get(self, index = None): 
    if index is None:
      return self.stack
    else:
      return self.stack[index]