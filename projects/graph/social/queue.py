from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):  # => O(1)
    
    # Use add_to_tail method from LinkedList to add to the queue
    # Increment size by 1 for every enqueue
    
    self.storage.add_to_tail(item)  # O(1)
    self.size += 1  # O(1)
  
  def dequeue(self): # => O(1)
    
    # Use remove_head method to dequeue
    # Want to return the dequeued_item because the test expects a return value
    # Decrement size by 1 for every dequeue as long as the size is not 0
    
    dequeued_item = self.storage.remove_head()  # O(1)
    
    if self.size > 0:  # O(1)
      self.size -= 1  # O(1)
    
    return dequeued_item  # O(1)
    

  def len(self): # => O(1)
    
    # Return the queue's size
    
    return self.size
