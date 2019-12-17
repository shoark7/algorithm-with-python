"""Implement custom deck data structure

url: https://www.acmicpc.net/problem/10866
"""
from collections import deque
import sys

input = sys.stdin.readline


class Deque:
    EMPTY_MESSAGE = -1

    def __init__(self):
        self._deque = deque([])

    def back(self):
        return self._deque[-1] if not self.empty() else self.EMPTY_MESSAGE

    def empty(self):
        return 1 if self.size() == 0 else 0

    def front(self):
        return self._deque[0] if not self.empty() else self.EMPTY_MESSAGE

    def pop_front(self):
        return self._deque.popleft() if not self.empty() else self.EMPTY_MESSAGE

    def pop_back(self):
        return self._deque.pop() if not self.empty() else self.EMPTY_MESSAGE

    def push_back(self, v):
        v = int(v)
        self._deque.append(v)

    def push_front(self, v):
        v = int(v)
        self._deque.appendleft(v)

    def size(self):
        return len(self._deque)


if __name__ == '__main__':
    deck = Deque()
    N = int(input())

    for _ in range(N):
        cmd = input().strip().split()
        cmd.append('')

        v = eval('deck.' + cmd[0] + '(' + cmd[1] + ')')
        if v is not None:
            print(v)
