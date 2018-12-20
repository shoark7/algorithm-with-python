"""Implement treap data structure in Python"""

import random


class Node:
    def __init__(self, v):
        self._value = v
        self._size = 1
        self._right = None
        self._left = None
        self._priority = random.random()

    @property
    def priority(self):
        return self._priority

    @property
    def value(self):
        return self._value

    @property
    def size(self):
        return self._size

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node
        self._calc_size()

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
        self._calc_size()

    def _calc_size(self):
        self._size = 1
        if self.left:
            self._size += self.left.size
        if self.right:
            self._size += self.right.size


def split(root, key):
    if root is None:
        return None, None

    if root.value < key:
        left, right = split(root.right, key)
        root.right = left
        return root, right
    else:
        left, right = split(root.left, key)
        root.left = right
        return left, root


def insert(root, node):
    if root is None:
        return node

    if root.priority < node.priority:
        left, right = split(root, node.value)
        node.left = left
        node.right = right
        return node
    elif node.value < root.value:
        root.left = insert(root.left, node)
    else:
        root.right = insert(root.right, node)
    return root


def merge(a, b):
    if a is None:
        return b
    elif b is None:
        return a

    if a.priority < b.priority:
        b.left = merge(a, b.left)
        return b
    else:
        a.right = merge(a.right, b)
        return a


def erase(root, v):
    if root.value == v:
        return merge(root.left, root.right)
    elif root.value > v:
        root.left = erase(root.left, v)
    else:
        root.right = erase(root.right, v)
    return root


def kth(root, k):
    left_size = 0
    if root.left is not None:
        left_size = root.left.size

    if k <= left_size:
        return kth(root.left, k)
    elif k == left_size + 1:
        return root
    else:
        return kth(root.right, k - left_size - 1)


def count_less_than(root, v):
    if root is None:
        return 0

    if root.value >= v:
        return count_less_than(root.left, v)
    else:
        ls = root.left.size if root.left else 0
        return ls + 1 + count_less_than(root.right, v)


def min_bigger_than(root, x, parent=None):
    if root.value > x:
        if not root.left:
            return root
        else:
            return min_bigger_than(root.left, x, root)
    else:
        if not root.right:
            return parent if parent.value > x else None
        else:
            return min_bigger_than(root.right, x, root)


def max_smaller_than(root, x, parent=None):
    if root is None:
        return None

    if root.value < x:
        cand = max_smaller_than(root.right, x, root)
        return root if not cand else cand
    else:
        cand = max_smaller_than(root.left, x, root)
        if not cand:
            return parent if parent.value < x else None
        else:
            return cand



def max_in_tree(root):
    if root is None:
        return None

    if max_in_tree(root.right):
        return max_in_tree(root.right)
    else:
        return root


def min_in_tree(root):
    if root is None:
        return None

    if min_in_tree(root.left):
        return min_in_tree(root.left)
    else:
        return root


def does_tree_have(root, x):
    if root is None:
        return False

    if root.value == x:
        return True
    elif root.value > x:
        return does_tree_have(root.left, x)
    else:
        return does_tree_have(root.right, x)
