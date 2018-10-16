"""
Simple graph implementation compatible with BokehGraph class.
"""
import random


# Linked List
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
    new_node = Node(value, None)
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.set_next(new_node)
      self.tail = new_node

  def remove_head(self):
    if not self.head:
      return None
    if not self.head.get_next():
      head = self.head
      self.head = None
      self.tail = None
      return head.get_value()
    value = self.head.get_value()
    self.head = self.head.get_next()
    return value

  def contains(self, value):
    if not self.head:
      return False
    current = self.head
    while current:
      if current.get_value() == value:
        return True
      current = current.get_next()
    return False

  def get_max(self):
    if not self.head:
      return None
    max_value = self.head.get_value()
    current = self.head.get_next()
    while current:
      if current.get_value() > max_value:
        max_value = current.get_value()
      current = current.get_next()
    return max_value


# Stack
class Stack:
  def __init__(self):
    self.size = 0
    self.storage = []
  
  def last_in(self, value):
    self.storage.append(value)
    self.size += 1

  def first_out(self):
    if self.size > 0:
      self.size -= 1
      return self.storage.pop()


# Queue
class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, value):
    self.storage.add_to_tail(value)
    self.size += 1
  
  def dequeue(self):
    if self.size > 0:
      self.size -= 1
    return self.storage.remove_head()

  def len(self):
    return self.size


# Graph
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        """
        Create an empty graph
        """
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        """
        Add an vertex to the graph
        """
        self.vertices[vertex_id] = Vertex(vertex_id)
    
    def add_edge(self, v1, v2):
        """
        Add an undirected edge to the graph
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    
    def add_directed_edge(self, v1, v2):
        """
        Add a directed edge to the graph
        """
        if v1 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist!")
    
    def dft(self, starting_node, visited=None):
        if visited is None:
            visited = Stack()
        visited.last_in(starting_node)
        while visited.size > 0:
            current_node = visited.first_out()

    
    def bft(self, starting_node):
        # create an empty queue
        q = Queue()
        q.enqueue(starting_node)
        visited = []
        while q.size > 0:
            current_node = q.dequeue()




# Vertex
class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
        """
        Create an empty vertex
        """
        self.id = vertex_id
        self.edges = set()
        if x is None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y is None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y
    
    def __repr__(self):
        return f"{self.edges}"
