from linked_list import LinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def enqueue(self, item):
        self.size += 1
        return self.storage.add_to_tail(item)

    def dequeue(self):
        if self.size:
            self.size -= 1
            return self.storage.remove_head()
        return None

    def len(self):
        return self.size
