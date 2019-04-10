"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
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
    new_node = Node(value)
    if self.head is None: #LL has no nodes
      self.head = new_node
    else: 
      self.tail.set_next(new_node)
    self.tail = new_node

  def remove_head(self):
    if self.head is None: #LL has no nodes
      return None
    elif self.head.next_node is None: #LL has only one node prior to removal
      rtrn_val = self.head.value
      self.head = None
      self.tail = None
      return rtrn_val
    else:
      rtrn_val = self.head.value
      nxt_node = self.head.next_node
      self.head = nxt_node
      return rtrn_val

  def contains(self, value):
    # if head is none, return false
    # otherwise
    # starting at head, check every node
    # repeat until value is found or next_node is None
    if self.head is None:
      return False
    else:
      wasFound = False
      cur_node = self.head
      while wasFound is False:
        if cur_node is None:
          break
        elif cur_node.value == value:
          wasFound = True
        
        cur_node = cur_node.next_node

    return wasFound

  def get_max(self):
    # starting at head, store largest value
    # go through each node comparing to current largest
    # update as necessary
    # return largest when next_node is None
    if self.head is not None:
      cur_head = self.head
      cur_max = cur_head.value

      while cur_head.next_node is not None:
        cur_head = cur_head.next_node
        if cur_head.value > cur_max:
          cur_max = cur_head.value
      
      return cur_max



 