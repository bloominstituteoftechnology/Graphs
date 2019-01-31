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
        # create a new node
        node = Node(value)
        # if the LL is not empty
        if self.tail:
            # then set the tail's next to the new node
            self.tail.set_next(node)
        else:
            # if it is empty, set the new node to the head
            self.head = node
        # set the LL's tail to the new node
        self.tail = node

    def remove_head(self):
        # check if the head is None
        if self.head:
            # set the head node's next node value to a temp var
            old_head = self.head
            # del the head node
            del self.head
            # then set head to that temp
            self.head = old_head.next_node

            if self.head is None:
                self.tail = None

            return old_head.value

    def contains(self, value):
        # set the current node to the head
        curr_node = self.head
        while True:
            # 1. if the node is None, return False
            if curr_node is None:
                return False
            elif curr_node.value == value:
                # 2. if the node's value matches the query value, return True
                return True
            else:
                curr_node = curr_node.next_node

    def get_max(self):
        if self.head:
            # set initial max value to head
            current = self.head
            max_value = current.value

            while current:  # while current is not None
                if max_value < current.value:
                    max_value = current.value

                # keep going to the next node
                current = current.get_next()

            return max_value
        else:
            return None
