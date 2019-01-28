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
        node = Node(value)

        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            self.tail = node

    def remove_head(self):
        if self.head == None:
            return None
        if not self.head.get_next():
            old_head = self.head
            self.head = None
            self.tail = None
            return old_head.get_value()
        else:
            head_value = self.head.get_value()
            self.head = self.head.get_next()
            return head_value

    def contains(self, value):
        curr_node = self.head

        while True:

            if curr_node is None:
                return False
            elif curr_node.value == value:
                return True
            else:
                curr_node = curr_node.next_node

    def get_max(self):

        if self.head is None:
            return None

        node_head = self.head
        value = node_head.get_value()

        while node_head.get_next() is not None:
            node_head = node_head.get_next()

            if node_head.get_value() > value:
                value = node_head.get_value()

        return value
