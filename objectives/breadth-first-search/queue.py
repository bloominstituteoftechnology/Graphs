"""
This module will feature a Queue data structure
"""

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        """Create a new node 
           Assign it's next reference to None
           Set the next reference of the tail to point to this new node.
           then update the tail reference itself to this new node. 
           error messages will occur without an inital check for the head and tail
           if the head and tail is none that means the linkedlist is empyt so the first item has to be both the head and the tail. 
        """
        new_node = Node(value)
        new_node.set_next(None)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        """
        set the head to the next node 
        error messages will occur without an inital check for the head. 
        """
        if self.head == None:
            return self.head 
        else:
            returning = self.head.get_value()
            self.head = self.head.get_next()
            if self.head is None:
                self.tail = None
            return returning

    def contains(self, value):
        current = self.head
        if current is None:
            return None
        else:
            while True:
                if value == current.get_value():
                    return True
                current = current.get_next()
                if current is None:
                    return False
                    break

    def get_max(self):
        max_value = -10000
        current = self.head
        if current is None:
            return None
        else:
          while True:
              if current.get_value() > max_value:
                  max_value = current.get_value()
              current = current.get_next()
              if current is None:
                  return max_value


class Queue:
    def __init__(self, max_size=None):  # Allows for bounded queues.
        self.size = 0
        self.max_size = max_size
        self.storage = LinkedList()

    def enqueue(self, item):
        if self.has_space():
            self.storage.add_to_tail(item) #since we are using self.storage = LinkedList()
                # also need to self.tail.set_next_node(item)
            self.size += 1
            
        else:
            print("The queue has no more room!")

    def dequeue(self):
        if self.len() > 0:
            popped = self.storage.remove_head()
            self.size -= 1
            return popped
        else:
            print("This queue is totally empty!")

    def len(self):
        return self.size

    def peek(self):
        # return self.head.get_value()
        """Peek at the head without removing it. """
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.head.get_value()

    def has_space(self):
      # prevents queue overflow
        """  it allows us to see if we can enqueue() a new value on the end of the queue.  """
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.len()

    def is_empty(self):
        return self.size == 0
        # this is neccessary because you cannot remove from a
        # empty list or you get queue underflow
