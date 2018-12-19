"""Print the sequence of pre, in, postorder traversal of a binary tree

:input:
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

:return:
ABDCEFG
DBAECFG
DBEGFCA

url: https://www.acmicpc.net/problem/1991
"""
import string


def traverse(root, nodes, direction):
    ans = ''
    def find(root):
        nonlocal ans
        if root is None:
            return

        cha, left, right = nodes[root]
        if direction == 'pre':
            ans += cha
            find(left)
            find(right)
        elif direction == 'in':
            find(left)
            ans += cha
            find(right)
        else:
            find(left)
            find(right)
            ans += cha
    find(root)
    return ans


if __name__ == '__main__':
    CAPS = string.ascii_uppercase
    N = int(input())
    nodes = [None for _ in range(N)]

    for _ in range(N):
        parent, left, right = input().split()
        left = CAPS.index(left) if left != '.' else None
        right = CAPS.index(right) if right != '.' else None
        nodes[CAPS.index(parent)] = [parent, left, right]

    print(traverse(0, nodes, 'pre'))
    print(traverse(0, nodes, 'in'))
    print(traverse(0, nodes, 'post'))
