class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, item):
        self.storage.append(item)
        return
  
    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.pop()
        else:
            return None