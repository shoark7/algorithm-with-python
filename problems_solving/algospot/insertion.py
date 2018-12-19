"""Return sequence of original array before insertion sort

:input:
2
5
0 1 1 2 3
4
0 1 2 3

:return:
5 1 4 3 2
4 3 2 1

url: https://algospot.com/judge/problem/read/INSERTION
ID : INSERTION
"""
import random


def split(root, key):
    if root is None:
        return (None, None)

    if root.value < key:
        left, right = split(root.right, key)
        root.set_right(left)
        return root, right
    else:
        left, right = split(root.left, key)
        root.set_left(right)
        return left, root


def insert(root, node):
    if root is None:
        return node

    if root.priority < node.priority:
        left, right = split(root, node.value)
        node.set_left(left)
        node.set_right(right)
        return node
    elif node.value < root.value:
        root.set_left(insert(root.left, node))
    else:
        root.set_right(insert(root.right, node))
    return root


def merge(a, b):
    # We assume min value of subtree b is bigger than max value of subtree a
    if a is None:
        return b
    if b is None:
        return a
    if a.priority < b.priority:
        b.set_left(merge(a, b.left))
        return b
    else:
        a.set_right(merge(a.right, b))
        return a


def erase(root, key):
    if root is None:
        return root
    if root.value == key:
        ret = merge(root.left, root.right)
        return ret
    if key < root.value:
        root.set_left(erase(root.left, key))
    else:
        root.set_right(erase(root.right, key))
    return root


def count_less_than(root, x):
    if root is None:
        return 0
    if root.value >= x:
        return count_less_than(root.left, x)
    ls = root.left.size if root.left is not None else 0
    return ls + 1 + count_less_than(root.right, x)


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


class TreapNode:
    def __init__(self, v):
        self.value = v
        self.priority = random.random()
        # size means number of nodes of a subtree which root is itself
        self.size = 1
        self.left = None
        self.right = None

    def set_left(self, new_node):
        self.left = new_node
        self.calc_size()

    def set_right(self, new_node):
        self.right = new_node
        self.calc_size()

    def calc_size(self):
        self.size = 1
        if self.left:
            self.size += self.left.size
        if self.right:
            self.size += self.right.size


def before_sort(shifted):
    N = len(shifted)
    ans = [0] * N
    root = TreapNode(1)

    for i in range(1, N):
        root = insert(root, TreapNode(i+1))

    for i in range(N-1, -1, -1):
        larger = shifted[i]
        k = kth(root, i + 1 - larger)
        ans[i] = k.value
        root = erase(root, k.value)

    return ans


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        input()
        shifted = [int(n) for n in input().split()]
        ans.append(before_sort(shifted))

    for n in ans:
        print(' '.join(str(c) for c in n))
