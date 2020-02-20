
# Note: This Queue class is sub-optimal. Why?

class LinkNode():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def insertBefore(self, node):
        node.prev = self.prev
        node.next = self
        self.prev = node

    def insertAfter(self, node):
        node.next = self.next
        node.prev = self
        self.next = node

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def addToHead(self, value):
        newNode = LinkNode(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.insertBefore(newNode)
            self.head = newNode
        self.count += 1

    def removeFromHead(self):
        oldHead = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = oldHead.next
            self.head.prev = None
        if oldHead is not None:
            self.count -= 1
            return oldHead.value
        else:
            return None

    def addToTail(self, value):
        newNode = LinkNode(value)
        if self.tail is None:
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.insertAfter(newNode)
            self.head = newNode
        self.count += 1

    def removeFromTail(self):
        oldTail = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = oldTail.prev
            self.tail.next = None
        if oldTail is not None:
            self.count -= 1
            return oldTail.value
        else:
            return None


class Queue():
    def __init__(self):
        # self.queue = []
        self.storage = LinkedList()
    def enqueue(self, value):
        self.storage.addToHead(value)
    def dequeue(self):
        return self.storage.removeFromTail()
    def size(self):
        return self.storage.count

class Stack():
    def __init__(self):
        self.storage = LinkedList()
    def push(self, value):
        self.storage.addToTail(value)
    def pop(self):
        return self.storage.removeFromTail()
    def size(self):
        return self.storage.count
