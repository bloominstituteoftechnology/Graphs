class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def size(self):
        return len(self.queue)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0) #dequeue gives first element and delete it from queue.
        else:
            return "Empty Queue"
    
    def is_Empty(self):
        if len(self.queue) == 0:
            return True
        return False
