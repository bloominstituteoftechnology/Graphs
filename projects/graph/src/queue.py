class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    def enqueue(self, item):
        self.storage.append(item)
        self.size += 1
    def dequeue(self):
        if self.size:
            self.size-= 1
        return self.storage.pop(0)
    def len(self):
        return self.size