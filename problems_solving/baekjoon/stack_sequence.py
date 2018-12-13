"""Return order of pop, push ops to make given arr

:input:
8
4
3
6
8
7
5
2
1

:return:
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-

url: https://www.acmicpc.net/problem/1874
"""
import sys
sys.setrecursionlimit(10 ** 6)


class Stack:
    def __init__(self, arr=[]):
        self._stack = list(arr)
        self._len = len(self._stack)

    def pop(self):
        if self._len == 0:
            raise ValueError("Stack is empty")

        v = self._stack.pop()
        self._len -= 1
        return v

    def push(self, v):
        self._stack.append(v)
        self._len += 1

    def is_empty(self):
        return self._len == 0


def calc_order(arr):
    N = len(arr)
    orders = []
    stack = Stack()
    possible = True

    def generate(i, now):
        nonlocal possible
        if i == N:
            return
        if now <= arr[i]:
            while now <= arr[i]:
                stack.push(now)
                orders.append('+')
                now += 1
            stack.pop()
            orders.append('-')
            generate(i+1, now)
        else:
            popped = stack.pop()
            orders.append('-')
            if popped != arr[i]:
                possible = False
                return
            else:
                generate(i+1, now)

    generate(0, 1)
    return (possible, orders) if possible else (possible, [])


if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    possible, ans = calc_order(arr)

    if possible:
        for n in ans:
            print(n)
    else:
        print('NO')
