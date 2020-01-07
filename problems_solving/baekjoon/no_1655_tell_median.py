"""Tell running median of each input in array

url: https://www.acmicpc.net/problem/1655
"""
from heapq import heappop, heappush
import sys

input = sys.stdin.readline


if __name__ == '__main__':
    max_heap, min_heap = [], []
    N = int(input())

    # Loop invariant
    # max_heap as A, min_heap as B
    #
    # 1. MAX(A) <= MIN(B)
    # 2. |A| - |B| <= 1
    # 3. left median is MAX(A)
    for _ in range(N):
        n = int(input())

        if len(max_heap) == len(min_heap):
            if min_heap and n > min_heap[0]:
                v = heappop(min_heap)
                heappush(max_heap, -v)
                heappush(min_heap, n)
            else:
                heappush(max_heap, -n)
        else: # size of max heap is 1 bigger than min heap
            if max_heap and -max_heap[0] > n:
                v = -heappop(max_heap)
                heappush(max_heap, -n)
                heappush(min_heap, v)
            else:
                heappush(min_heap, n)

        print(-max_heap[0])
