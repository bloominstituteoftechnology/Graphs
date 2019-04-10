class Stack:
    def __init__(self):
        self.storage = []

    def add_to_tail(self, item):
        self.storage.append(item)
    
    def remove_from_tail(self):
        return self.storage.pop()

    def len(self):
        return len(self.storage)