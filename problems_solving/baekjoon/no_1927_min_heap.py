"""Implement min heap

url: https://www.acmicpc.net/problem/1927
"""
from heapq import *
import sys

input = sys.stdin.readline


def do_calculations(cmds, min_heap=True):
    POPOUT = 0
    ret = []
    heap = []

    for cmd in cmds:
        if cmd == POPOUT:
            if not heap:
                ret.append(0)
            else:
                _, value = heappop(heap)
                ret.append(value)
        else:
            priority = cmd if min_heap else -cmd
            heappush(heap, (priority, cmd))

    return ret


if __name__ == '__main__':
    N = int(input())
    cmds = []

    for _ in range(N):
        cmds.append(int(input().strip()))

    for r in do_calculations(cmds, min_heap=True):
        print(r)
