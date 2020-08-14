"""
Implementations of FIFO queue and LIFO stack classes (objects).
"""
class Queue():
    """
    A FIFO queue.
    """
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
    def __repr__(self):
        return f"Queue (FIFO): {self.queue}"

class Stack():
    """
    A LIFO stack.
    """
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
    def __repr__(self):
        return f"Stack (LIFO): {self.stack}"
