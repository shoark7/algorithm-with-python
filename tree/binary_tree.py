"""Binary Tree in Python


"""


class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def append(node):
        def _append(data):
            if not self.root.left and not self.root.right:
                node.left = Node(data, parent=node)
            elif self.root.left and not self.root.right:
                node.right = Node(data, parent=node)
            else:
                _append(node.left)
        _append(data)
