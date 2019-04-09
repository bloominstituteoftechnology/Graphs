class Stack:
    def __init__(self):
        self.storage = []

    def push(self, item):
        self.storage.append(item)
        return
  
    def pop(self):
        if len(self.storage) > 0:
            return self.storage.pop(-1)
        else:
            return None