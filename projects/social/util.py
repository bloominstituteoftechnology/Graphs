
# Note: This Queue class is sub-optimal. Why?
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
    def peek(self, idx):
        # idx out of bounds?
        if idx > len(self.queue)-1:
            # index value does not refer to a valid queue element
            print("index value: {i} does not refer to a valid queue element".format(i=idx))
            return None

        return self.queue[idx]

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
    # peek returns the next element to be popped (e.g. for inspection)
    def is_empty(self):
        if len(self.stack) == 0:
            return True

        return False
