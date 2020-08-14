
# Note: This Queue class is sub-optimal. Why?

# we're using an array for the Queue which means we need to pop from the front, the remaining values need to
# move over 1 at a time.  This is O(n) complexity.
# this should be O(1) or constant.  That's what is important about a queue.
# Needs to be a linked list (circular linked list?) / dictionary. 

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

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

