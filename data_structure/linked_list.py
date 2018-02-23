"""Linked list in Python


Date: 2018/02/23
"""


class Node:
    """Node object containing value and next element"""
    def __init__(self, value):
        """Node must be initialized with a value"""
        self.value = value
        self.next = None


class Linked_list:
    """Single linked list in Python"""
    def __init__(self, value=None):
        self.length = 0
        self.head = None
        self.tail = None

        if value:
            self.length += 1
            node = Node(value)
            self.head = node
            self.tail = node

    def _check_index(self, index):
        """Check if given index is valid for the list now
        It checks
            1. whether index is bigger than list's length
            2. whether index is smaller than 0
            3. or the list is empty
        """
        if self.length <= index or index < 0:
            raise ValueError("Given index isn't valid now")
        elif self.length == 0:
            raise ValueError("List is empty")
        else:
            return

    def append(self, value):
        """Append a value to the tip of the list"""
        node = Node(value)
        if not self.length:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.length += 1

    def get(self, index):
        """Get the value of given index in the list"""
        self._check_index(index)

        i = 0
        node = self.head
        while i < index:
            node = node.next
            i += 1

        return node.value

    def delete(self, index):
        """Delete the value of given index in the list"""
        self._check_index(index)
        i = 0
        node = self.head
        while i < index - 1:
            node = node.next
            i += 1

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            if index == 0:
                self.head = self.head.next
            elif index == self.length - 1:
                self.tail = node
            else:
                node.next = node.next.next
        self.length -= 1

    def modify(self, index, value):
        """Change the value of nth node with given value"""
        self._check_index(index)
        i = 0
        node = self.head
        while i < index:
            node = node.next
            i += 1

        node.value = value
