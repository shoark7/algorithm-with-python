"""Get sum of running medians

:input:
3
10 1 0
10 1 1
10000 1273 4936

:return:
19830
19850
2448920

url: https://algospot.com/judge/problem/read/RUNNINGMEDIAN
ID : RUNNINGMEDIAN
"""
import heapq


def sum_medians(N, a, b, D=20090711, seed=1983):
    def rng(a, b):
        s = seed
        while True:
            ret = s
            s = (s * a + b) % D
            yield ret

    number_generator = rng(a, b)
    ans = 0
    max_heap = []
    min_heap = []

    for _ in range(N):
        n = next(number_generator)
        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, (-n, n))
        else:
            heapq.heappush(min_heap, (n, n))

        if max_heap and min_heap and min_heap[0][1] < max_heap[0][1]:
            a = heapq.heappop(max_heap)[1]
            b = heapq.heappop(min_heap)[1]
            heapq.heappush(max_heap, (-b, b))
            heapq.heappush(min_heap, (a, a))
        ans = (ans + max_heap[0][1]) % D
    return ans


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        N, a, b = (int(n) for n in input().split())
        ans.append(sum_medians(N, a, b))

    for n in ans:
        print(n)
