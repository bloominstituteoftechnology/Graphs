class Queue:
    def __init__(self):
        self.storage = []
        self.count = 0

    def enqueue(self, item):
        self.storage.append(item)
        self.count += 1
        return
  
    def dequeue(self):
        if self.count > 0:
            self.count -= 1
            return self.storage.pop()
        else:
            return None

    def length(self):
        return self.count