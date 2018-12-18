"""Return result of postorder traversal of binary tree

:input:
2
7
27 16 9 12 54 36 72
9 12 16 27 36 54 72
6
409 479 10 838 150 441
409 10 479 150 838 441

:return:
12 9 16 36 72 54 27
10 150 441 838 479 409

url: https://algospot.com/judge/problem/read/TRAVERSAL
ID : TRAVERSAL
"""
def make_post(preorder, inorder):
    N = len(preorder)
    if not preorder:
        return
    root = preorder[0]

    L = 0
    while L < N:
        if inorder[L] == root:
            break
        L += 1

    make_post(preorder[1:L+1], inorder[:L])
    make_post(preorder[L+1:], inorder[L+1:])

    print(root, end=' ')


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        N = int(input())
        preorder = [int(n) for n in input().split()]
        inorder = [int(n) for n in input().split()]
        make_post(preorder, inorder)
        print()
