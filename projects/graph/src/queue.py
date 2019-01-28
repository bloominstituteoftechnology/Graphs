
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if self.size() > 0:
            return self.queue[0]
        else:
            return None
    
    def is_Empty(self):
        if self.size() == 0:
            return False
        else:
            return True
    
    def size(self):
        return len(self.queue)




