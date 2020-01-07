"""Implement Absolute heap

url: https://www.acmicpc.net/problem/11286
"""
from heapq import heappop, heappush
import sys

input = sys.stdin.readline


POPOUT = 0


if __name__ == '__main__':
    heap = []
    N = int(input())

    for _ in range(N):
        n = int(input())
        if n != POPOUT:
            heappush(heap, (abs(n), n))
        else:
            if heap:
                _, v = heappop(heap)
                print(v)
            else:
                print(0)
