
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if len(self.queue > 0):
            return queue[0]
        else:
            return None
    
    def is_Empty(self):
        if len(self.queue) == 0:
            return False
        else:
            return True


