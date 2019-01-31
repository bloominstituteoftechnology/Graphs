"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node  # pointer to the next, pointer is a memory address

  def get_value(self):  # O(1)
    return self.value

  def get_next(self):  # O(1)
    return self.next_node

  def set_next(self, new_next):  # O(1)
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None  # first item
    self.tail = None  # last item

  def add_to_tail(self, value):  # => O(1)
    
    # Create a new node
    # If the tail doesn't exists, meaning the list is empty, since we are adding a new node, the head and tail will be set to the new node  
    # Else, set the tail's next node to be the new node  
    
    new_node = Node(value)    # new_node = Node(value, None) O(1)
    
    if self.tail is None:  # O(1)
      self.head = new_node
      self.tail = new_node
    else:  # tail exists
      self.tail.set_next(new_node)  # tell existing tail that next node is the new one, O(1)
      self.tail = new_node # new tail
    
  def remove_head(self):  # => O(1)
    
    # Check if the head doesn't exist, return none
    # If the head exists, 
      # save it to a temperary head and get its value
    # Set the new head to be the temperary head's next node
    # Delete the old head
    # Return the old value because the test expects a return value to compare
    
    if self.head is None:
      return None
    
    old_head = self.head
    old_value = old_head.get_value()
    self.head = old_head.get_next()
    
    # After changing the head, if the head is now none, also set the tail to none because the list is now empty
    if self.head is None:
      self.tail = None
      
    del(old_head)
      
    return old_value  # test expects us to return the old head value
    
    # the old head is still there, but the head pointer is directed at the next node.
    # after the method finishes, python will clean up the old head (sometime in the future) since nothing is referencing it anymore
    # to get rid of the old head completely, we do something like: del(old_head)
    
              
  def contains(self, value):  # => O(n)
  
  # best case: you get the value right away, O(1)
  # worse case: you have to go through the entire queue, O(n)
  # average case: add all the possibilities up and divide by number of possibilities, O(n/2)
    
    # Set the current node to the head
    # Do a while loop
      # If the current node doesn't exist, return false
      # Compare the current node's value to the query value, return true if they are equalled
      # Set the current node to be the next node
    
    current_node = self.head  # O(1)
    
    while True:  # O(n), as long as there is node
      if current_node is None:  # O(1)
        return False
      elif current_node.get_value() == value:  # O(1)
        return True
      else:
        current_node = current_node.get_next()  # O(1)

  def get_max(self):
    
    # Create a variable to hold the max, initialize it with None
    # Get the current node
    # Do while loop to check if the current node exist
      # If it exists, check if there is a current max or if the current node's value is greater than the current max
        # If either of these case is true, set the current max to be the current node's value
      # Set the current node to be the next node
    # Return the current max
    
    current_max = None
    current_node = self.head
    
    while current_node is not None:
      if current_max is None or current_node.get_value() > current_max:
        current_max = current_node.get_value()
        
      current_node = current_node.get_next()
    
    return current_max
      
#ll = LinkedList()
#ll.add_to_tail(5)
#print(ll.head.value)
#ll.tail
#print(ll.tail.value)
#ll.add_to_tail(6)
#print(ll.head.value)
#print(ll.tail.value)
#print(ll.head.next_node.value)
#ll.remove_head()
#print(ll.head.value)
#print(ll.tail.value)

